# Contributing to {{ cookiecutter.repo_name }} <!-- omit from toc -->

This is a guide for developers contributing to the project.

## Contents <!-- omit from toc -->

- [Dependencies](#dependencies)
  - [`uv`](#uv)
- [Contributing](#contributing)
  - [Tasks](#tasks)
  - [Submitting changes](#submitting-changes)
  - [Code formatting, linting and type checking](#code-formatting-linting-and-type-checking)
  - [Tests](#tests)
  - [Updating documentation](#updating-documentation)

## Dependencies

### `uv`

Install [`uv` from here](https://docs.astral.sh/uv/getting-started/installation/)

Once installed you can synchronise the project via:

```
uv sync
```

To add dependencies, i.e., those that are explicitly required for the source code (found in [`src`](../src/)):

```
uv add <package>
```

To add developer dependencies, i.e., for development purposes and not required for the package to function independently:

```
uv add <package> --dev
```

In both cases if a specific version is required then specify it via `<package>==<version>`

## Contributing

### Tasks

The tool `taskipy` is included as a developer dependency. It has a number of tasks that can be run via `uv run task <task_name>`. You can see the available tasks by running:

```
uv run task --list
```

**Note**: If you have the virtual environment already activated (in VSCode for example), you can run the tasks directly via `task <task_name>`.

### Submitting changes

Any changes on the repository must come from a Pull Request (PR), specifying in there what the new changes are with this nomenclature:

- `feat/<name>`: A new feature is implemented in the PR. It can also include bug fixes for other features, but please specify that in the description.
- `bug/<name>`: When fixing bugs please do not label them as features, as they will be prioritised.

Merge commits should follow the [commitlint](https://commitlint.js.org/) format.

It's recommended that branches used for PRs are like this: `[feat/bug]-short-title-in-kebab-case`.

All changes will need to be reviewed by, at least, one project owner before they are merged to main.

### Code formatting, linting and type checking

Code **must** be correctly **formatted**, **linted** and **no type checking errors** must occur when deploying it. It's checked upon committing[^1] and active PRs to be merged into `main`. Please check the [`pyproject.toml`](../pyproject.toml) file for more information about the conventions used.

### Tests

We **strongly encourage** tests added when new features are added and bugs are fixed. Generally, a PR will not be accepted if it doesn't contain relevant tests. Please have a look at the [tests](../tests/) subfolder to see how tests are managed. You can run the tests either via `pytest` or `uv run task test`.

### Updating documentation

Any important design and/or architectural decisions made that impact algorithms or software architecture should be captured via lightweight decisions records. See [here](../decisions/0001-record-decisions.md) for an example to follow.

Functions and classes must be appropriately described via docstrings and the [sphinx](https://www.sphinx-doc.org/en/master/#user-guide) documentation that is generated must be valid[^2].

[^1]: Pre-commit is used to run linting, formatting, and styling.

[^2]: API documentation can be generated via `uv run task docs` with .rst files under `docs/modules` and the rendered html available under `public` (both are git ignored as per the [.gitignore](./.gitignore)).
