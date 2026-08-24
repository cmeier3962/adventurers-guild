from enum import StrEnum


# ---------- Adventurer ---------- #
class AdventurerStatus(StrEnum):
    """Available statuses for adventurers."""

    AVAILABLE = "Available"
    ASSIGNED = "Assigned"
    INJURED = "Injured"
    RETIRED = "Retired"


# ---------- Quest ---------- #
class QuestDifficulty(StrEnum):
    """Available difficulties for quests."""

    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    ELITE = "Elite"
    MASTER = "Master"


class QuestStatus(StrEnum):
    """Available statuses for quest progress."""

    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


# ---------- Items / Equipment ---------- #
class ItemType(StrEnum):
    """Available item categories."""

    WEAPON = "Weapon"
    ARMOR = "Armor"
    ACCESSORY = "Accessory"
    CONSUMABLE = "Consumable"
    MATERIAL = "Material"
    QUEST = "Quest"
    CURRENCY = "Currency"


class ItemRarity(StrEnum):
    """Available item rarities."""

    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EXOTIC = "Exotic"
    ASCENDED = "Ascended"
    LEGENDARY = "Legendary"


class EquipmentSlot(StrEnum):
    """Available equipment slots."""

    HEAD = "Head"
    CHEST = "Chest"
    HANDS = "Hands"
    LEGS = "Legs"
    FEET = "Feet"
    BACK = "Back"
    RING_1 = "Ring 1"
    RING_2 = "Ring 2"
    AMULET = "Amulet"
    MAIN_HAND = "Main Hand"
    OFF_HAND = "Off Hand"


# ---------- Stats ---------- #
class StatType(StrEnum):
    """Available statistics used throughout Eryndor."""

    HEALTH = "Health"
    ATTACK = "Attack"
    DEFENSE = "Defense"


# ---------- Jobs ---------- #
class RoleType(StrEnum):
    """Available job roles."""

    TANK = "Tank"
    HEALER = "Healer"
    DPS = "DPS"


class DamageStyle(StrEnum):
    """Available combat damage styles."""

    MELEE = "Melee"
    MARKSMAN = "Marksman"
    ARCANE = "Arcane"


class JobCategory(StrEnum):
    """Available job categories."""

    COMBAT = "Combat"
    GATHERING = "Gathering"
    CRAFTING = "Crafting"


class JobTier(StrEnum):
    """Available job tiers."""

    FOUNDATION = "Foundation"
    ADVANCED = "Advanced"


class JobType(StrEnum):
    """Available jobs."""

    # Foundation Jobs
    DEFENDER = "Defender"
    ACOLYTE = "Acolyte"
    MARTIALIST = "Martialist"
    MARKSMAN = "Marksman"
    MYSTIC = "Mystic"
