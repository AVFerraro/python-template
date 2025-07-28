# Project start-up

This file contains the detailed instructions to start-up a new project. It should be deleted, once the start-up is completed, since it is no longer useful[^1].

## Prerequisites

If the steps under "Prerequisites" in the [template README](https://github.com/AVFerraro/python-template) have been followed to get to this stage, then the following are already satisfied:

- `uv` installed

## Prepare files

- Remove files/directories that won't be used.
- Rename files/directories to increase specifity as needed.
- Review [pyproject.toml](./pyproject.toml) and update the configuration of the Python code module. **Note** you may need to update the project URL.
- Review [README.md](./README.md) and [CONTRIBUTING.md](./CONTRIBUTING.md) and update with information on how the project is organised, its purpose, how it operates, etc.

## Prepare first commit

Initialise git:

```
git init -b main
```

Lock the Python dependencies and instantiate `pre-commit`:

```
uv sync
uv run task setup
```

Add all files to git:

```
git add -A
```

Check all files pass inspection:

```
uv run task check
```

Check the basic tests pass:

```
uv run task test
```

Create the first commit and push to `origin` on Evinova GitHub:

```
git commit -m "chore: initialise project"
git remote add origin {{ cookiecutter.project_repo }}
git push -u origin main
```

## Setup IDE extensions

- Set the default interpreter to the virtual environment's Python interpreter associated with {{ cookiecutter.package_name }}
  - If this is configured then any tasks can be run without the `uv run` prefix. E.g., `uv run task check` can be run as `task check`.
- Set the testing suite to use `pytest` pointing to the [tests](./tests/) directory

## Clean-up

Delete this file as it is no longer needed and should not be included in the repository[^1].

[^1]: This file is git-ignored.
