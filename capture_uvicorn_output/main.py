"""Entry point for the main application loop.

You can customize this file to your liking, or indeed empty it entirely and
start from scratch.
Note that if you remove the 'App' class entirely, you will need to remove the
`[tool.poetry.scripts]` section from pyproject.toml as well (if it exist).
"""


class App:
    """Main application class."""

    def __init__(self) -> None:
        """Initialize the application."""

    def __call__(self) -> None:
        """Call the application."""
        print("Welcome to Capture Uvicorn Output!")  # noqa: T201


app = App()


if __name__ == "__main__":
    app()
