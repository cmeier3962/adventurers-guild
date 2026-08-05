import pytest

from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, AdventurerStatus


### ---------- Initialize Class Tests---------- ###
def test_adventurer() -> None:
    """Tests a pre-defined adventurer."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    assert adventurer.adventurer_id == "adv-001"
    assert adventurer.username == "Nox"
    assert adventurer.adventurer_class == AdventurerClass.WARRIOR
    assert adventurer.level == 1
    assert adventurer.status == AdventurerStatus.AVAILABLE


### ---------- Username Tests---------- ###
def test_username_whitespace_only() -> None:
    """Tests that a ValueError is raised when a username is empty."""
    with pytest.raises(ValueError, match="Username cannot be empty"):
        Adventurer("adv-001", "   ", AdventurerClass.WARRIOR, 1)


def test_username_length_short() -> None:
    """Tests that a ValueError is raised when the length of a username is too short."""
    with pytest.raises(ValueError, match="Username must be between 3 and 15 characters"):
        Adventurer("adv-001", "No", AdventurerClass.WARRIOR, 1)


def test_username_length_long() -> None:
    """Tests that a ValueError is raised when the length of a username is too long."""
    with pytest.raises(ValueError, match="Username must be between 3 and 15 characters"):
        Adventurer("adv-001", "Noxtrum1234567890", AdventurerClass.WARRIOR, 1)
        

### ---------- Level Up Tests---------- ###
def test_level_up() -> None:
    """Tests that the adventurer levels up by 1."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.level_up()
    assert adventurer.level == 2


def test_level_low() -> None:
    """Tests that a ValueError triggers for an invalid level."""
    with pytest.raises(ValueError, match="Level must be greater than zero"):
        Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 0)


def test_level_up_while_retired() -> None:
    """Tests that a retired adventurer cannot level up."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.retire()
    assert adventurer.status == AdventurerStatus.RETIRED
    
    with pytest.raises(ValueError, match="Retired adventurers cannot level up"):
        adventurer.level_up()
    
    assert adventurer.level == 1


### ---------- Status Tests---------- ###
def test_status_injured() -> None:
    """Tests that the initial status is available and then updated to injured."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    assert adventurer.status == AdventurerStatus.AVAILABLE
    
    adventurer.injured()
    assert adventurer.status == AdventurerStatus.INJURED


def test_status_recovered() -> None:
    """Tests that the initial status is injured and then updated to available."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.injured()
    assert adventurer.status == AdventurerStatus.INJURED
    
    adventurer.recover()
    assert adventurer.status == AdventurerStatus.AVAILABLE


def test_status_recover_invalid() -> None:
    """Tests that a non-injured adventurer cannot recover."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    with pytest.raises(ValueError, match="Only injured adventurers can recover"):
        adventurer.recover()


def test_status_retired() -> None:
    """Tests that the status is updated to retired."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.retire()
    assert adventurer.status == AdventurerStatus.RETIRED


def test_status_retired_to_injured() -> None:
    """Tests that the adventurer's status is already retired and then fails to change to injured."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.retire()
    assert adventurer.status == AdventurerStatus.RETIRED

    with pytest.raises(ValueError, match="Retired adventurers cannot be injured"):
        adventurer.injured()


def test_status_injured_to_injured() -> None:
    """Tests that an already-injured adventurer cannot be injured again."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.injured()
    assert adventurer.status == AdventurerStatus.INJURED

    with pytest.raises(ValueError, match="The adventurer is already injured"):
        adventurer.injured()


def test_status_retired_to_retired() -> None:
    """Tests that an already-retired adventurer cannot retire again."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer.retire()
    assert adventurer.status == AdventurerStatus.RETIRED
    
    with pytest.raises(ValueError, match="The adventurer is already retired"):
        adventurer.retire()