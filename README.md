# Eryndor: The Shattered Veil

Eryndor is a Python learning project focused on building a growing fantasy RPG domain model through object-oriented design, testing, and incremental system development.

The project currently models adventurers, parties, quests, items, inventories, rewards, and character progression. Equipment support is now being introduced.

The long-term goal is to expand Eryndor into a larger RPG system with equipment, combat, enemies, bosses, dungeons, loot systems, crafting, persistence, APIs, and potentially a game client.

---

# Current Features

## Adventurers

Adventurers currently have:

- a unique ID
- a validated username
- an adventurer class
- a status
- an inventory
- a progression component
- derived experience and level properties
- a collection of unclaimed reward items

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

- becoming injured
- recovering from injury
- retiring
- preventing invalid status transitions
- receiving items through their inventory
- gaining experience through progression
- receiving rewards
- preserving reward items that do not fit in inventory
- retrying unclaimed items when inventory space becomes available

Each adventurer receives their own inventory and progression object.

Adventurers can also accept a custom inventory when created, allowing inventory behavior to be tested independently and reused by future systems.

---

## Character Progression

Character progression is managed by a dedicated `Progression` component rather than storing level directly on `Adventurer`.

Progression currently supports:

- starting at zero experience by default
- optional custom starting experience
- preventing negative starting experience
- adding experience
- preventing negative experience gains
- deriving level dynamically from total experience

The current level curve is:

```text
XP required for level N = 100 × (N - 1)²
```

Examples:

| Level | Total XP Required |
|------:|------------------:|
| 1 | 0 |
| 2 | 100 |
| 3 | 400 |
| 4 | 900 |
| 5 | 1600 |

Experience is the stored source of truth. Level is calculated from experience so the two values cannot become inconsistent.

`Adventurer` exposes convenience properties for both experience and level while delegating progression logic to the `Progression` component.

---

## Inventory

Inventories store and manage items owned by adventurers and other future game systems.

Inventories currently support:

- configurable capacity
- tracking stored items
- reporting current item count
- reporting available slots
- checking whether the inventory is full
- adding items when space is available
- removing items by item ID
- returning success or failure from item operations

Supported behaviors include:

- preventing items from being added when inventory is full
- confirming successful item additions and removals
- maintaining separate inventories between adventurers

The inventory system is designed as a reusable component that may later support:

- player banks
- familiar inventories
- guild storage
- reward containers
- loot systems
- equipment interaction

The current inventory implementation stores items in a simple list. Manual inventory positioning, sorting, and persistent slot locations have not been implemented yet.

---

## Items

Items currently have:

- a unique ID
- a validated name
- a validated description
- an item type
- a rarity
- a value
- an optional equipment slot

Available item types:

- Weapon
- Armor
- Accessory
- Consumable
- Material
- Quest
- Currency

Available item rarities:

- Common
- Uncommon
- Rare
- Exotic
- Ascended
- Legendary

Available equipment slots:

- Head
- Chest
- Hands
- Legs
- Feet
- Back
- Ring
- Amulet
- Main Hand
- Off Hand

Current equipment-slot rules:

- Weapons may use Main Hand or Off Hand
- Armor may use Head, Chest, Hands, Legs, or Feet
- Accessories may use Back, Ring, or Amulet
- Weapons, armor, and accessories must have an equipment slot
- Non-equippable item types cannot have an equipment slot
- Invalid item-type and equipment-slot combinations raise an error

Items currently provide the foundation for future systems including:

- equipment
- item stats
- bonuses and effects
- durability
- crafting
- loot drops
- rewards

---

## Rewards

`Reward` is a reusable object representing rewards earned from gameplay activities.

Rewards currently support:

- experience rewards
- item rewards
- experience and items together
- empty/default rewards
- preventing negative experience rewards
- copying supplied item lists so reward contents remain independent from the caller's list

Rewards are designed to eventually support multiple reward sources such as:

- quests
- bosses
- dungeons
- events
- daily or weekly activities
- loot containers

### Reward Handling

Adventurers can receive a `Reward`.

When a reward is received:

1. Reward experience is added to the adventurer's progression.
2. Each reward item is individually offered to the adventurer's inventory.
3. Items that fit are stored normally.
4. Items that do not fit are preserved in `unclaimed_items`.

Unclaimed items can later be retried through the adventurer's claim behavior.

This prevents earned items from being silently destroyed when inventory space is unavailable.

A dedicated loot chest, bank overflow, or reward-claim interface may replace or expand this behavior later.

---

## Parties

Parties group adventurers together for quest and future gameplay systems.

Parties currently support:

- validated party names
- a maximum party size
- adding members
- removing members
- available-slot tracking
- full-party detection
- leader assignment
- leader changes
- preventing invalid party operations
- updating adventurer statuses as members are assigned or removed

Parties currently support up to four adventurers.

---

## Quests

Quests currently support:

- validated names and descriptions
- quest difficulty
- reusable `Reward` objects
- quest status
- party assignment
- starting quests
- completing quests
- abandoning quests
- validating quest state transitions
- requiring a valid party and leader before assignment

Available quest states include:

- Not Started
- In Progress
- Completed

Quest rewards are modeled, but quest completion does not yet automatically distribute rewards to party members.

Reward distribution rules for parties will be designed later so item ownership and shared rewards can be handled intentionally.

---

# Equipment System — In Progress

Equipment development has started.

Current groundwork includes:

- `EquipmentSlot` enum
- `Accessory` item type
- item equipment-slot assignment
- validation of item type and compatible equipment slots

The next planned component is a dedicated `Equipment` class.

The intended direction is:

```text
Adventurer
├── Inventory
├── Progression
├── Equipment
└── Unclaimed Items
```

The equipment system will eventually track one equipped item per equipment slot.

Initial equipment behavior is expected to include:

- equipping an item from inventory
- removing the equipped item from inventory
- detecting an already occupied equipment slot
- returning the previously equipped item to inventory
- equipping the replacement item
- unequipping items back into inventory

Exact inventory positioning is intentionally deferred. The current inventory does not model persistent visual slots, so unequipped items can simply return to the inventory collection.

Future equipment behavior may include:

- two-handed weapons
- shields
- dual wielding
- class or level requirements
- equipment stats
- item bonuses
- set bonuses

---

# Planned Features

## Equipment

- dedicated `Equipment` component
- equipping and unequipping items
- occupied-slot replacement
- two-handed weapons
- equipment requirements
- equipment stats and bonuses
- set bonuses

## Character Systems

- attributes and combat stats
- health and resources
- class progression
- specializations
- additional progression tracks if they become necessary

The current scope intentionally uses only overall adventurer experience and level.

## Inventory

- item stacking
- bag-based inventory capacity
- additional bag slots
- inventory sorting
- persistent inventory positions
- banks
- guild storage
- familiar storage

## Reward and Loot Systems

- reward claiming interfaces
- loot chests
- boss-specific loot tables
- rare-drop indicators
- bad-luck protection
- currencies
- reputation
- bank or storage overflow behavior

## Gameplay Systems

- enemies and monsters
- combat
- bosses
- dungeons
- loot tables
- crafting
- gathering
- quests and progression integration

## Application Systems

- persistence
- database integration
- APIs
- FastAPI
- authentication
- potential game client or interface

---

# Current Architecture

```text
Adventurer
├── Inventory
│   └── Items
├── Progression
│   ├── Experience
│   └── Derived Level
├── Unclaimed Items
└── Equipment              <- in progress

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
└── EquipmentSlot
```

A major design goal is to keep responsibilities separated between reusable components rather than placing all game logic directly inside `Adventurer`.

---

# Project Structure

```text
.
├── src/
│   └── eryndor/
│       ├── __init__.py
│       ├── adventurer.py
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
│   ├── test_inventory.py
│   ├── test_item.py
│   ├── test_party.py
│   ├── test_progression.py
│   ├── test_quest.py
│   └── test_reward.py
├── README.md
└── pyproject.toml
```

An `equipment.py` module will be added as the equipment system is implemented.

---

# Testing and Code Quality

The project uses:

- pytest
- pytest-cov
- shared pytest fixtures through `conftest.py`
- parametrized tests where multiple inputs share the same behavior
- Ruff for linting and formatting
- Pyright for static type checking
- uv for Python environment and dependency management

The project currently maintains full test coverage while new systems are developed incrementally.

Typical local checks:

```powershell
ruff check .
ruff format .
pyright
pytest
```

---

# Learning Goals

Eryndor is being built primarily as a hands-on learning project.

Current learning areas include:

- object-oriented programming
- domain modeling
- class composition
- delegation
- dependency injection
- separation of responsibilities
- derived properties and single sources of truth
- enums and state transitions
- type annotations
- validation and exception handling
- mutable-object behavior
- collection handling
- pytest unit testing
- parametrized testing
- reusable pytest fixtures
- test ownership and avoiding redundant tests
- branch coverage
- dependency management with uv
- linting and formatting with Ruff
- static type checking with Pyright
- Git and GitHub workflows
- feature-branch development
- software architecture and system design
- future API development with FastAPI

The project intentionally starts with simple implementations and revisits earlier systems for refactoring as new requirements emerge.
