# Adventurer's Guild

The project currently models adventurers, parties, and quests through a tested Python domain model. 

The long-term goal is to expand it with inventories, equipment, skills, quest chains, persistence, and a FastAPI application.

## Current features

### Adventurers

Adventurers currently have:

- a unique ID
- a validated username
- an adventurer class
- a level
- a status

Available adventurer classes:

- Warrior
- Mage
- Rogue
- Cleric
- Ranger

Available statuses:

- Available
- Assigned
- Injured
- Retired

Supported behaviors include:

- leveling up
- becoming injured
- recovering from injury
- retiring
- preventing invalid status transitions

### Parties

Parties currently support:

- validated party names
- a maximum size of four adventurers
- adding available adventurers
- preventing duplicate members
- removing members
- assigning one party leader
- replacing an existing party leader
- automatically clearing the leader when they leave
- tracking member count
- reporting available member slots
- reporting whether the party is full

Adding an adventurer to a party changes their status from `AVAILABLE` to `ASSIGNED`.

Removing an adventurer changes their status back to `AVAILABLE`.

### Quests

Quests currently have:

- a unique ID
- a validated name
- a validated description
- a difficulty
- a gold reward
- a progress status

Available quest difficulties:

- Easy
- Normal
- Hard
- Elite
- Master

Available quest statuses:

- Not Started
- In Progress
- Completed

Supported behaviors include:

- starting a quest
- completing a quest
- abandoning an active quest
- preventing invalid status transitions

New quests begin with a status of `NOT_STARTED`.

Starting a quest changes its status to `IN_PROGRESS`.

Only quests currently in progress can be completed. Completing a quest changes its status to `COMPLETED`.

Abandoning an active quest returns its status to `NOT_STARTED`, allowing it to be accepted again later.

## Planned features

Future development may include:

- assigning parties to quests
- quest prerequisites and quest chains
- adventurer-level requirements for quests
- skill requirements for quests
- inventory and equipment management
- items and item categories
- quest rewards beyond gold
- guild-wide adventurer, party, and quest management
- FastAPI endpoints
- Pydantic request and response models
- SQLite persistence
- SQLAlchemy integration

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── scripts/
│   └── smoke_test.py
├── src/
│   └── adventurers_guild/
│       ├── __init__.py
│       ├── __main__.py
│       ├── adventurer.py
│       ├── enums.py
│       ├── main.py
│       ├── party.py
│       └── quest.py
├── tests/
│   ├── test_adventurer.py
│   ├── test_main.py
│   ├── test_party.py
│   └── test_quest.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

## Requirements

- Git
- Python 3.14
- `uv`

Install `uv` on Windows with WinGet:

```powershell
winget install --id astral-sh.uv -e
```

Restart the terminal after installation, then verify:

```powershell
uv --version
```

## Set up the project

Clone the repository:

```powershell
git clone https://github.com/cmeier3962/adventurers-guild.git
cd adventurers-guild
```

Synchronize the environment:

```powershell
uv sync
```

This command creates the project virtual environment and installs the project and its development dependencies.

You do not normally need to activate `.venv` manually.

## Run the project

Run the package:

```powershell
uv run python -m adventurers_guild
```

Run the smoke-test script:

```powershell
uv run python scripts\smoke_test.py
```

## Run tests

Run the complete test suite:

```powershell
uv run pytest
```

The project requires at least 80% test coverage.

Run one test file without enforcing project-wide coverage:

```powershell
uv run pytest tests\test_party.py --no-cov
```

## Code-quality checks

Run Ruff linting:

```powershell
uv run ruff check .
```

Automatically repair safe lint violations:

```powershell
uv run ruff check . --fix
```

Run static type checking:

```powershell
uv run pyright
```

Run the complete local validation:

```powershell
uv run ruff check .
uv run pyright
uv run pytest
```

## Development workflow

Development is completed on feature branches and merged into `main` through pull requests.

Example:

```powershell
git switch -c feature/example-feature
git push -u origin feature/example-feature
```

Before committing:

```powershell
uv run ruff check .
uv run pyright
uv run pytest
```

Then commit and push:

```powershell
git add -A
git commit -m "Describe the completed change"
git push
```

GitHub Actions runs the configured quality checks for pull requests targeting `main`.

## Learning goals

This project is being used to practice:

- object-oriented design
- composition between classes
- enums and state transitions
- type annotations
- validation and exception handling
- pytest unit testing
- test coverage
- dependency management with `uv`
- linting with Ruff
- static type checking with Pyright
- Git and GitHub workflows
- API development with FastAPI