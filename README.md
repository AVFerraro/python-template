# Python Template Repository <!-- omit from toc -->

This Python template is a cookiecutter project designed to expedite PoCs, MVPS, or any project startup. Follow the [prerequisites](#prerequisites) for [creating a new project](#create-a-new-project) to quickly render a structured repository in minutes.

## Contents <!-- omit from toc -->

- [Features](#features)
- [Prerequisites](#prerequisites)
  - [install `uv` + `cookiecutter`](#install-uv--cookiecutter)
- [Create a new project](#create-a-new-project)


## Features

- Organised project and data structure with dedicated directories for:
  - Analysis scripts and notebooks
  - Data (input, interim, output)
  - Decision records
  - API documentation (using [sphinx](https://www.sphinx-doc.org/en/master/))
  - Source code (with a dedicated package configured)
  - Tests (with unit tests for project source code created using [pytest](https://docs.pytest.org/en/stable/))
- `.editorconfig` using [Editor Config](https://editorconfig.org/) for consistent editor settings across different editors[^1]
- `.env` for environment variables loaded in scripts (not source code) using [python-dotenv](https://pypi.org/project/python-dotenv/)
- `.gitattributes` for consistent line endings across different operating systems
- `.gitignore` for ignoring common files and directories in Python projects
- `.here` marker for project root detection using [pyprojroot](https://pypi.org/project/pyprojroot/)
- `.pre-commit-config.yaml` for managing [pre-commit](https://pre-commit.com/) hooks[^1]
- `.talismanrc` for secrets protection using [Talisman](https://github.com/thoughtworks/talisman)[^1]
- `CONTRIBUTING.md` for developer guidance on contributing
- `LICENSE` file for software licensing
- `pyproject.toml` for Python [project configuration](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
  - Dependency management using [uv](https://docs.astral.sh/uv/)
  - Task management using [taskipy](https://pypi.org/project/taskipy/)
  - Linting and formatting with [ruff](https://docs.astral.sh/ruff/)[^1]

This template is based on the popular [DrivenData Cookiecutter DataScience](https://github.com/drivendata/cookiecutter-data-science): a logical, reasonably standardised, but flexible, project structure for doing and sharing data science work.

## Prerequisites

The Python Template requires the following:

### install `uv` + `cookiecutter`

Install [`uv` from here](https://docs.astral.sh/uv/getting-started/installation/)

Once installed you can install [`cookiecutter`](https://pypi.org/project/cookiecutter/) as a tool (including the [`jinja2-git` extension](https://pypi.org/project/jinja2-git/))

```
uv tool install cookiecutter --with jinja2-git
```

## Create a new project

To start a new project, run the following in the directory where you want to create the project:

```
cookiecutter https://github.com/AVFerraro/python-template
```

Answer the command line prompts pertaining to information needed about your new repository (defaults are shown in <span style="color:#29B8DB">blue</span>).

Then, follow the instructions in the [START.md](./{{%20cookiecutter.repo_name%20}}/START.md) file in the new project directory.

[^1]: These developer dependencies are handled via [`pre-commit`](https://pre-commit.com/) hooks.
