# Capture Uvicorn Output <!-- omit in toc -->

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
$ python capture_output/main.py
```

## License

This project is released under the terms of the MIT license.

## Credits

The original Python boilerplate for this package was created using
[Pymaker](https://github.com/seapagan/py-maker) by [Grant
Ramsay](https://github.com/seapagan) (me :smile:)
