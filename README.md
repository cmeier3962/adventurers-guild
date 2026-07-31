# Python Project Template

A modern starting point for Python projects using:

- Python 3.14
- `uv` for Python and dependency management
- the `src/` package layout
- Ruff for linting and formatting
- Pyright for static type checking
- Pytest for automated testing
- pytest-cov for coverage reporting
- GitHub Actions for continuous integration

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── scripts/
│   └── smoke_test.py
├── src/
│   └── your_project/
│       ├── __init__.py
│       ├── __main__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

### What belongs where

- `src/your_project/`: application or reusable package code
- `tests/`: automated tests
- `scripts/`: optional development and maintenance scripts
- `.github/workflows/`: GitHub Actions workflows
- `pyproject.toml`: project metadata, dependencies, and tool configuration
- `uv.lock`: exact resolved dependency versions

## Requirements

Install:

- Git
- `uv`

`uv` can also install and manage the Python version required by the project.

### Install uv on Windows

Using WinGet:

```powershell
winget install --id astral-sh.uv -e
```

Restart the terminal after installation, then verify:

```powershell
uv --version
```

## Create a project from this template

Create a new repository using this template, then clone it:

```powershell
git clone <repository-url>
cd <repository-name>
```

Rename the package directory:

```powershell
Rename-Item src\your_project src\my_project
```

Use lowercase letters and underscores for the Python package directory.

Update the following values:

1. Change `name` in `pyproject.toml`.
2. Change the Hatch package path in `pyproject.toml`.
3. Change the coverage package name in `pyproject.toml`.
4. Replace imports containing `your_project`.
5. Update the project title and description in this README.

## Set up the project

Synchronize the environment:

```powershell
uv sync
```

This command:

- reads `pyproject.toml`
- installs the required Python version when necessary
- creates `.venv`
- installs the project and development dependencies
- updates `uv.lock`

You do not normally need to activate `.venv` manually.

## Run the application

Run the package:

```powershell
uv run python -m your_project
```

Run the smoke-test script:

```powershell
uv run python scripts\smoke_test.py
```

## Run automated tests

```powershell
uv run pytest
```

The project requires at least 80% test coverage.

## Run code-quality checks

Lint the project:

```powershell
uv run ruff check .
```

Automatically repair safe lint violations:

```powershell
uv run ruff check . --fix
```

Format the project:

```powershell
uv run ruff format .
```

Check formatting without modifying files:

```powershell
uv run ruff format --check .
```

Run static type checking:

```powershell
uv run pyright
```

## Recommended local validation

Before committing changes, run:

```powershell
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
```

These are also run automatically by GitHub Actions.

## Dependency management

Add a runtime dependency:

```powershell
uv add requests
```

Add a development dependency:

```powershell
uv add --dev pytest
```

Remove a dependency:

```powershell
uv remove requests
```

Update compatible dependency versions:

```powershell
uv lock --upgrade
uv sync
```

Inspect the dependency tree:

```powershell
uv tree
```

Avoid editing `uv.lock` manually.

## uv compared with traditional pip

A traditional Python workflow often requires several separate steps:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python script.py
```

With `uv`, the equivalent workflow is usually:

```powershell
uv sync
uv run python script.py
```

`uv` manages the virtual environment, Python version, dependencies, and lockfile as one project workflow.

## Continuous integration

The GitHub Actions workflow runs on pushes and pull requests targeting `main`.

It verifies:

- dependencies match `uv.lock`
- Ruff linting passes
- Ruff formatting passes
- Pyright type checking passes
- Pytest and coverage requirements pass

A pull request should not be merged until these checks succeed.