# Eryndor

Eryndor is a Python-based RPG foundation project focused on learning
object-oriented programming, software architecture, testing practices,
and game system design.

The goal of this project is to build a scalable RPG framework inspired
by games such as RuneScape, Final Fantasy XIV, and other MMO/RPG systems
while continuously improving code quality and design patterns.

This project is currently focused on backend game logic and domain
modeling. Future goals may include transitioning concepts into C++ and
Unreal Engine as a long-term game development learning project.

------------------------------------------------------------------------

## Current Features

### Adventurer System

-   Adventurer creation and validation
-   Adventurer classes
-   Adventurer status management
-   Experience and progression tracking
-   Inventory and equipment ownership

### Inventory System

-   Configurable inventory capacity
-   Add and remove item functionality
-   Inventory space validation
-   Support for unclaimed items when inventory space is unavailable

### Item System

-   Item creation and validation
-   Item types:
    -   Weapons
    -   Armor
    -   Accessories
    -   Consumables
-   Item rarity system
-   Equipment slot validation
-   Item stat bonuses

### Equipment System

-   Equipment slot management:
    -   Head
    -   Chest
    -   Hands
    -   Legs
    -   Feet
    -   Back
    -   Ring 1
    -   Ring 2
    -   Amulet
    -   Main Hand
    -   Off Hand
-   Equipping and unequipping items
-   Replacing existing equipped items
-   Equipment stat aggregation

### Stats System

-   Reusable stat management system
-   Supported statistics:
    -   Health
    -   Attack
    -   Defense
-   Adding and retrieving stat values
-   Validation against invalid negative stat values
-   Designed to support future adventurer stats, equipment bonuses,
    buffs, and derived statistics

### Quest and Reward Systems

-   Quest creation and progression
-   Reward handling
-   Experience rewards
-   Item rewards
-   Handling unclaimed rewards when inventory space is unavailable

------------------------------------------------------------------------

## Development Tools

This project uses modern Python development practices:

-   Python 3.14
-   uv for environment and dependency management
-   pytest for testing
-   pytest-cov for coverage reporting
-   Ruff for linting and formatting
-   Pyright for static type checking
-   GitHub Actions for continuous integration

------------------------------------------------------------------------

## Testing

The project uses automated tests to validate functionality and prevent
regressions.

Current testing includes:

-   Object initialization
-   Validation rules
-   Success and failure cases
-   Edge cases
-   Integration between systems

The project maintains 100% test coverage.

------------------------------------------------------------------------

## Project Structure

    src/
    └── eryndor/
        ├── adventurer.py
        ├── equipment.py
        ├── enums.py
        ├── inventory.py
        ├── item.py
        ├── progression.py
        ├── quest.py
        ├── reward.py
        └── stats.py

    tests/
    ├── test_adventurer.py
    ├── test_equipment.py
    ├── test_inventory.py
    ├── test_item.py
    ├── test_party.py
    ├── test_progression.py
    ├── test_quest.py
    ├── test_reward.py
    └── test_stats.py

------------------------------------------------------------------------

## Future Roadmap

Planned systems include:

### Character Development

-   Base adventurer statistics
-   Level-based stat growth
-   Character attributes
-   Class-specific progression
-   Derived statistics

### Combat Systems

-   Damage calculations
-   Attack and defense mechanics
-   Critical hits
-   Abilities and skills
-   Status effects

### RPG Systems

-   Enemies and creatures
-   Boss encounters
-   Dungeons
-   Loot tables
-   Crafting
-   Economy systems

### Long-Term Goals

-   Rebuild core systems in C++
-   Learn Unreal Engine development
-   Create a playable 3D RPG prototype
-   Integrate art, assets, and gameplay systems

------------------------------------------------------------------------

## Development Philosophy

Eryndor is built incrementally with a focus on:

-   Clean object-oriented design
-   Separation of responsibilities
-   Maintainable architecture
-   Strong typing
-   Automated testing
-   Continuous refactoring

The goal is not only to create a game system, but to learn the
engineering principles behind building large-scale software.
