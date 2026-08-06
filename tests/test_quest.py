import pytest

from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, AdventurerStatus, QuestDifficulty, QuestStatus
from adventurers_guild.party import Party
from adventurers_guild.quest import Quest


### ---------- Initialize Class Tests---------- ###
def test_quest() -> None:
    """Tests the creation of a Quest object."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.quest_id == "quest-001"
    assert quest.name == "New Beginnings"
    assert quest.description == "This quest will be the start of the tutorial."
    assert quest.difficulty is QuestDifficulty.EASY
    assert quest.reward_gold == 100
    assert quest.status is QuestStatus.NOT_STARTED


def test_quest_zero_gold() -> None:
    """Tests the creation of a Quest object with a gold reward of zero."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                0,
            )
    assert quest.reward_gold == 0


def test_quest_negative_gold() -> None:
    """Test to fail creating a Quest object when reward_gold is negative."""
    with pytest.raises(ValueError, match="Gold reward must be zero or higher"):
        Quest(
            "quest-001", 
            "New Beginnings", 
            "This quest will be the start of the tutorial.", 
            QuestDifficulty.EASY, 
            -100,
        )


### ---------- Quest Name Tests ---------- ###
def test_quest_name_whitespace_only() -> None:
    """Tests that the quest name contains only whitespaces."""
    with pytest.raises(ValueError, match="Quest name cannot be empty"):
        Quest(
            "quest-001", 
            "   ", 
            "This quest will be the start of the tutorial.", 
            QuestDifficulty.EASY, 
            100,
        )


def test_quest_name_whitespace_before_after() -> None:
    """Tests that a quest name with leading and trailing whitespaces are removed."""
    quest = Quest(
                "quest-001", 
                "   New Beginnings   ", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.name == "New Beginnings"


def test_quest_name_length_short() -> None:
    """Tests that a quest name shorter than 3 characters is rejected."""
    with pytest.raises(ValueError, match="Quest name must be between 3 and 50 characters"):
        Quest(
            "quest-001", 
            "Ne", 
            "This quest will be the start of the tutorial.", 
            QuestDifficulty.EASY, 
            100,
        )


def test_quest_name_length_long() -> None:
    """Tests that a quest name longer than 50 characters is rejected."""
    name = "A" * 51
    with pytest.raises(ValueError, match="Quest name must be between 3 and 50 characters"):
        Quest(
            "quest-001", 
            name, 
            "This quest will be the start of the tutorial.", 
            QuestDifficulty.EASY, 
            100,
        )


### ---------- Quest Description Tests ---------- ###
def test_quest_description_whitespace_only() -> None:
    """Tests that the quest description contains only whitespaces."""
    with pytest.raises(ValueError, match="Quest description cannot be empty"):
        Quest(
            "quest-001", 
            "New Beginnings", 
            "     ", 
            QuestDifficulty.EASY, 
            100,
        )


def test_quest_description_whitespace_before_after() -> None:
    """Tests that a quest description with leading and trailing whitespaces are removed."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "     This quest will be the start of the tutorial.     ", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.description == "This quest will be the start of the tutorial."


def test_quest_description_length_short() -> None:
    """Tests that a quest description shorter than 10 characters is rejected."""
    with pytest.raises(ValueError, match="Quest description must be at least 10 characters"):
        Quest(
            "quest-001", 
            "New Beginnings", 
            "Quest", 
            QuestDifficulty.EASY, 
            100,
        )


### ---------- Quest Status Tests ---------- ###
def test_quest_status() -> None:
    """Verifies that quest status is not started and then updates status to in progress."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.status is QuestStatus.NOT_STARTED
    
    quest.start()
    assert quest.status is QuestStatus.IN_PROGRESS


def test_quest_status_already_started() -> None:
    """Starts the quest and then attempts to start it again while it is already in progress."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.status is QuestStatus.NOT_STARTED
    
    quest.start()
    assert quest.status is QuestStatus.IN_PROGRESS
    
    with pytest.raises(ValueError, match="Only quests that have not started can be started"):
        quest.start()
    

def test_quest_status_complete() -> None:
    """Tests to update the quest status to complete."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.status is QuestStatus.NOT_STARTED
    
    quest.start()
    assert quest.status is QuestStatus.IN_PROGRESS
    
    quest.complete()
    assert quest.status is QuestStatus.COMPLETED


def test_complete_quest_not_in_progress() -> None:
    """Tests that a quest cannot be completed before it is started."""
    quest = Quest(
                "quest-001", 
                "New Beginnings", 
                "This quest will be the start of the tutorial.", 
                QuestDifficulty.EASY, 
                100,
            )
    assert quest.status is QuestStatus.NOT_STARTED
    
    with pytest.raises(ValueError, match="Quests can only be completed if they are currently in progress"):
        quest.complete()
    
    assert quest.status is QuestStatus.NOT_STARTED