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