# Eryndor: The Shattered Veil

Eryndor is a Python learning project focused on building a growing
fantasy RPG domain model through object-oriented design, testing, and
incremental system development.

The project currently models adventurers, parties, quests, items,
inventories, rewards, character progression, and equipment systems.

The long-term goal is to expand Eryndor into a larger RPG system with
equipment, combat, enemies, bosses, dungeons, loot systems, crafting,
persistence, APIs, and potentially a game client.

------------------------------------------------------------------------

# Current Features

## Adventurers

Adventurers currently have:

-   a unique ID
-   a validated username
-   an adventurer class
-   a status
-   an inventory
-   an equipment system
-   a progression component
-   derived experience and level properties
-   a collection of unclaimed reward items

Available adventurer classes:

-   Warrior
-   Mage
-   Rogue
-   Cleric
-   Ranger

Supported behaviors include:

-   receiving items through their inventory
-   equipping and unequipping equipment
-   gaining experience through progression
-   receiving rewards
-   preserving reward items that do not fit in inventory
-   retrying unclaimed items when inventory space becomes available

Each adventurer receives their own inventory, equipment, and progression
objects.

------------------------------------------------------------------------

## Items

Items currently have:

-   a unique ID
-   a validated name
-   a validated description
-   an item type
-   a rarity
-   a value
-   an optional equipment slot
-   optional stat bonuses

Available item types:

-   Weapon
-   Armor
-   Accessory
-   Consumable
-   Material
-   Quest
-   Currency

Available stat types:

-   Attack
-   Defense
-   Health

Available equipment slots:

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

Current equipment-slot rules:

-   Weapons may use Main Hand or Off Hand
-   Armor may use Head, Chest, Hands, Legs, or Feet
-   Accessories may use Back, Ring 1, Ring 2, or Amulet
-   Weapons, armor, and accessories must have an equipment slot
-   Non-equippable item types cannot have an equipment slot
-   Invalid item-type and equipment-slot combinations raise an error

Items can provide stat bonuses through a flexible stat dictionary.

Example:

``` text
Novice Sword:
    Attack +5

Iron Helmet:
    Defense +10
    Health +25
```

Item stats provide the foundation for future systems including:

-   combat calculations
-   character attributes
-   equipment bonuses
-   set bonuses
-   item effects

------------------------------------------------------------------------

## Equipment System

The equipment system allows adventurers to equip items into dedicated
equipment slots.

Current functionality includes:

-   dedicated `Equipment` component
-   equipment slot tracking
-   equipping items
-   replacing already equipped items
-   unequipping items
-   returning unequipped items to inventory
-   checking occupied equipment slots
-   calculating combined equipment stats

The equipment structure is:

``` text
Adventurer
├── Inventory
├── Progression
├── Equipment
└── Unclaimed Items
```

Equipment currently supports:

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

Current behaviors:

-   Equipping an item removes it from inventory.
-   Equipping an item into an occupied slot returns the previous item.
-   Unequipping an item returns it to inventory.
-   Equipment calculates total bonuses from currently equipped items.

Future equipment behavior may include:

-   two-handed weapons
-   shields
-   dual wielding
-   class or level requirements
-   item durability
-   set bonuses
-   legendary effects

------------------------------------------------------------------------

# Current Architecture

``` text
Adventurer
├── Inventory
│   └── Items
├── Progression
│   ├── Experience
│   └── Derived Level
├── Equipment
│   └── Equipped Items
└── Unclaimed Items

Party
└── Adventurers

Quest
├── Party
└── Reward
    ├── Experience
    └── Items

Item
├── ItemType
├── ItemRarity
├── EquipmentSlot
└── Stats
    ├── Attack
    ├── Defense
    └── Health
```

A major design goal is to keep responsibilities separated between
reusable components rather than placing all game logic directly inside
`Adventurer`.

------------------------------------------------------------------------

# Project Structure

``` text
.
├── src/
│   └── eryndor/
│       ├── __init__.py
│       ├── adventurer.py
│       ├── equipment.py
│       ├── enums.py
│       ├── inventory.py
│       ├── item.py
│       ├── party.py
│       ├── progression.py
│       ├── quest.py
│       └── reward.py
├── tests/
│   ├── conftest.py
│   ├── test_adventurer.py
│   ├── test_equipment.py
│   ├── test_inventory.py
│   ├── test_item.py
│   ├── test_party.py
│   ├── test_progression.py
│   ├── test_quest.py
│   └── test_reward.py
├── README.md
└── pyproject.toml
```

------------------------------------------------------------------------

# Testing and Code Quality

The project uses:

-   pytest
-   pytest-cov
-   shared pytest fixtures through `conftest.py`
-   parametrized tests where multiple inputs share the same behavior
-   Ruff for linting and formatting
-   Pyright for static type checking
-   uv for Python environment and dependency management

The project currently maintains full test coverage while new systems are
developed incrementally.

Typical local checks:

``` powershell
ruff check .
ruff format .
pyright
pytest
```

------------------------------------------------------------------------

# Learning Goals

Eryndor is being built primarily as a hands-on learning project.

Current learning areas include:

-   object-oriented programming
-   domain modeling
-   class composition
-   delegation
-   dependency injection
-   separation of responsibilities
-   derived properties and single sources of truth
-   enums and state transitions
-   type annotations
-   validation and exception handling
-   mutable-object behavior
-   collection handling
-   pytest unit testing
-   parametrized testing
-   reusable pytest fixtures
-   branch coverage
-   dependency management with uv
-   linting and formatting with Ruff
-   static type checking with Pyright
-   Git and GitHub workflows
-   feature-branch development
-   software architecture and system design
-   designing interconnected game systems
-   composition over inheritance
-   aggregating and calculating derived data
-   future API development with FastAPI

The project intentionally starts with simple implementations and
revisits earlier systems for refactoring as new requirements emerge.
