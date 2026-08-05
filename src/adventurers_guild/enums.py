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
