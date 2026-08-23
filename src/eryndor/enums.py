from enum import StrEnum


class AdventurerClass(StrEnum):
    """Available adventurer classes."""

    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"
    CLERIC = "Cleric"
    RANGER = "Ranger"


class AdventurerStatus(StrEnum):
    """Available statuses for adventurers."""

    AVAILABLE = "Available"
    ASSIGNED = "Assigned"
    INJURED = "Injured"
    RETIRED = "Retired"


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
    """Available rarities for item drops."""

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


class StatType(StrEnum):
    """Available equipment stat bonuses."""

    ATTACK = "Attack"
    DEFENSE = "Defense"
    HEALTH = "Health"
