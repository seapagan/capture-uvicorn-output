"""Example of how to capture uvicorn output in a subprocess."""

from __future__ import annotations

import shutil
import signal
import subprocess
import sys
import threading
from pathlib import Path
from queue import Empty, Queue
from typing import IO, TYPE_CHECKING, Optional

from rich import print as rprint

if TYPE_CHECKING:
    from types import FrameType


class App:
    """Main application class."""

    subproc = None

    def __init__(self) -> None:
        """Initialize the application."""
        self.uvicorn_binary = self.get_uvicorn()

    def __call__(self) -> None:
        """Call the application."""
        if self.uvicorn_binary:
            # Start your process
            subproc = subprocess.Popen(
                [  # noqa: S603
                    self.uvicorn_binary,
                    "capture_output.server:api",
                    "--reload",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                encoding="utf-8",
            )

            signal.signal(signal.SIGINT, self.signal_handler)

            # Use a queue to handle the output
            q: Queue[str] = Queue()

            # Start a thread to enqueue the subprocess output
            t = threading.Thread(
                target=self.enqueue_output, args=(subproc.stdout, q)
            )
            t.daemon = True  # thread dies with the program
            t.start()

            # Read output in a non-blocking way. This is just an example, you
            # would send to logging or some other processing for a real
            # application.#
            try:
                while subproc.poll() is None:
                    try:
                        line = q.get_nowait()
                    except Empty:  # noqa: PERF203
                        pass  # No output yet
                    else:
                        rprint(line, end="")
            except KeyboardInterrupt:
                pass

            # Wait for the subprocess to finish if needed
            subproc.wait()

    def enqueue_output(self, out: IO[str], queue: Queue[str]) -> None:
        """Enqueue strings from an IO stream."""
        for line in iter(out.readline, b""):
            queue.put(line)
        out.close()

    def get_uvicorn(self) -> str | None:
        """Get uvicorn absolute path.

        We do it this way to avoid injection by changing the PATH.
        It's overkill but an example how to do it safer.
        """
        python_exe = sys.executable
        if python_exe:
            venv_path = Path(python_exe).parent
            return shutil.which("uvicorn", path=venv_path)
        return None

    def signal_handler(
        self, _sig: int | signal.Signals, _frame: Optional[FrameType]
    ) -> None:
        """Handle ctrl-c press gracefully.

        Instead of sending a `terminate()` to the process, we send a SIGINT
        (ctrl-c) which allows `uvicorn` to gracefully shut down and we can
        capture all the shutdown output.
        """
        print("\r", end="")  # remove the `^C` from the output  # noqa: T201
        rprint("[red]INFO:     Ctrl-C pressed, Shutting Down...")
        if self.subproc is not None:
            # Gracefully terminate the subprocess using sigint
            self.subproc.send_signal(signal.SIGINT)


app = App()


if __name__ == "__main__":
    app()
