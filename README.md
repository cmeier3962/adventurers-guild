# Eryndor: The Shattered Veil

The project currently models adventurers, parties, quests, items, and
inventories through a tested Python domain model.

The long-term goal is to expand it into a complete fantasy RPG system
with equipment, skills, combat, persistence, APIs, and potentially a
game client.

## Current features

## Adventurers

Adventurers currently have:

-   a unique ID
-   a validated username
-   an adventurer class
-   a level
-   a status
-   an inventory

Available adventurer classes:

-   Warrior
-   Mage
-   Rogue
-   Cleric
-   Ranger

Available statuses:

-   Available
-   Assigned
-   Injured
-   Retired

Supported behaviors include:

-   leveling up
-   becoming injured
-   recovering from injury
-   retiring
-   preventing invalid status transitions
-   receiving items through their inventory

Each adventurer is created with their own inventory by default.

Adventurers can also accept a custom inventory when created, allowing
inventory behavior to be reused across future systems such as banks,
familiars, or storage containers.

------------------------------------------------------------------------

## Inventory

Inventories store and manage items owned by adventurers and other game
systems.

Inventories currently support:

-   configurable capacity
-   tracking stored items
-   reporting current item count
-   reporting available slots
-   checking whether the inventory is full
-   adding items when space is available
-   removing items when they exist

Supported behaviors include:

-   preventing items from being added when the inventory is full
-   confirming successful item additions and removals
-   maintaining separate inventories between different adventurers

The inventory system is designed as a reusable component that can later
support:

-   player banks
-   familiar inventories
-   equipment storage
-   reward containers
-   loot systems

------------------------------------------------------------------------

## Items

Items currently have:

-   a unique ID
-   a validated name
-   a validated description
-   an item category
-   a rarity
-   a value

Available item types:

-   Weapon
-   Armor
-   Consumable
-   Material
-   Quest
-   Currency

Available item rarities:

-   Common
-   Uncommon
-   Rare
-   Exotic
-   Ascended
-   Legendary

Supported behaviors include:

-   validating item names
-   validating item descriptions
-   preventing negative item values
-   supporting zero-value items

Items currently represent the foundation for future systems including:

-   equipment
-   item bonuses
-   durability
-   crafting
-   loot drops
-   rewards

------------------------------------------------------------------------

# Planned features

Future development may include:

## Character progression

-   skills
-   experience
-   attributes
-   level requirements
-   class progression
-   specializations

## Inventory and equipment

-   item stacking
-   equipment slots
-   weapons and armor
-   item stats
-   bonuses and effects
-   durability
-   set bonuses

## Reward systems

-   reusable reward objects
-   quest rewards
-   dungeon rewards
-   boss loot
-   event rewards
-   currencies
-   reputation

## Gameplay systems

-   enemies and monsters
-   combat system
-   bosses
-   dungeons
-   loot tables
-   crafting
-   gathering

------------------------------------------------------------------------

# Project structure

``` text
.
├── src/
│   └── eryndor/
│       ├── adventurer.py
│       ├── enums.py
│       ├── inventory.py
│       ├── item.py
│       ├── party.py
│       └── quest.py
├── tests/
│   ├── test_adventurer.py
│   ├── test_inventory.py
│   ├── test_item.py
│   ├── test_party.py
│   └── test_quest.py
├── README.md
└── pyproject.toml
```

## Learning goals

This project is being used to practice:

-   object-oriented design
-   composition between classes
-   dependency injection
-   domain modeling
-   enums and state transitions
-   type annotations
-   validation and exception handling
-   pytest unit testing
-   reusable pytest fixtures
-   test coverage
-   dependency management with uv
-   linting with Ruff
-   static type checking with Pyright
-   Git and GitHub workflows
-   API development with FastAPI
-   software architecture and system design
