# Capture Uvicorn Output <!-- omit in toc -->

This repository is a template for a basic Python project using
[Poetry](https://python-poetry.org/), with assorted Linting and Testing
libraries installed as standard. It also uses
[pre-commit](https://pre-commit.com/).

- [Development setup](#development-setup)
  - [Task Runner](#task-runner)
  - [Linting](#linting)
  - [Pre-commit](#pre-commit)
- [License](#license)
- [Credits](#credits)

## Development setup

Install the dependencies using Poetry:

```console
$ poetry install
```

Then, activate the virtual environment:

```console
$ poetry shell
```

Now, you can start to code the meat of your application.

### Task Runner

The task-runner [Poe the Poet](https://github.com/nat-n/poethepoet) is installed
as a development dependency which allows us to run simple tasks (similar to npm
`scripts`).

These are run (from within the virtual environment) using the `poe` command and
then the script name, for example:

```console
$ poe pre
```

You can define your own, but there are 7 specific ones provided with the script.

- `pre` : Run `pre-commit run --all-files`
- `pylint`: Run Pylint on all Python files in the project.
- `mypy` = Run MyPy type-checker on all Python files in the project.
- `flake8` = Run Flake8 linter on all Python files in the project.
- `black` = Run Black code formatter on all Python files in the project.
- `try` = Run Tryceratops linter on all Python files in the project.

- `lint` = Runs pylint, mypy, flake8 and black in sequence

These are defined in the `pyproject.toml` file in the `[tool.poe.tasks]`
section. Take a look at this file if you want to add or remove tasks.

### Linting

This project includes [flake8](https://flake8.pycqa.org/en/latest/) (with
several plugins) for linting and
[Black](https://black.readthedocs.io/en/stable/) for formatting.
[Mypy](http://mypy-lang.org/) is installed for type checking.
[isort](https://pycqa.github.io/isort/),[Pylint](https://pylint.org/) and
[tyrceratops](https://github.com/guilatrova/tryceratops) are also installed as
standard.

### Pre-commit

There is a [pre-commit](https://pre-commit.com/) configuration provided to run
some checks on the code before it is committed.  This is a great tool to help
keep your code clean.

To install pre-commit, run the following command from inside your venv:

```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## License

This project is released under the terms of the  license.

## Credits

The original Python boilerplate for this package was created using
[Pymaker](https://github.com/seapagan/py-maker) by [Grant
Ramsay](https://github.com/seapagan)
