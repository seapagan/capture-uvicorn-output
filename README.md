# Capture Uvicorn Output

This is just an example of how to capture the `stdout` and `stderr` output of a
process and use it in a Python application.

It uses the [Threading](https://docs.python.org/3/library/threading.html) and
[Queue](https://docs.python.org/3/library/queue.html) modules to capture the
output of a [Uvicorn](https://www.uvicorn.org/) server and then use it in the
main application.

It also shows how to cleanly catch the ctrl-c keystroke and pass that on to the
`uvicorn` server to allow it and the application to shut down cleanly.

As a uvicorn server, it includes a simple API server based on
[FastAPI](https://fastapi.tiangolo.com/), though the same technique could be
used with most other types of processes.

## Setup

Install the dependencies using Poetry:

```console
$ poetry install
```

Then, activate the virtual environment:

```console
$ poetry shell
```

Now you can run the application:

```console
$ python main.py
```

## Code

The important code is in the `main.py` file, in the `__call__` method of the
App class. This method does the following:

- Set up the `uvicorn` server and start it.
- Sets up a `Queue` to capture the output.
- Start a separate thread to fill that queue from the `uvicorn` server's output.

The main thread then reads the output. from the queue and simply prints it for
now.

The `server.py` file just creates a very simple API server using `FastAPI` with
one route that returns a simple JSON response on the root
('<http://localhost:8000/>')

I will write a documentation page to explain this in more detail soon.

## Example Run

Below is an example of the output from running the application, showing the
`ctrl-c` being pressed and the application shutting down cleanly.

```console
$ python main.py
INFO:     Will watch for changes in these directories: ['/home/seapagan/code/capture-uvicorn-output']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [167389] using WatchFiles
INFO:     Started server process [167396]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:56914 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:46182 - "GET / HTTP/1.1" 200 OK
INFO:     Ctrl-C pressed, Shutting Down...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [167396]
INFO:     Stopping reloader process [167389]

```

## License

This project is released under the terms of the MIT license.

## Credits

The original Python boilerplate for this package was created using
[Pymaker](https://github.com/seapagan/py-maker) by [Grant
Ramsay](https://github.com/seapagan) (me :smile:)
