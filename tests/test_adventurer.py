import pytest

from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, AdventurerStatus


### ---------- Fixtures ---------- ###
@pytest.fixture
def adventurer() -> Adventurer:
    """Returns a valid available adventurer."""
    return Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)


### ---------- Initialize Class Tests ---------- ###
def test_adventurer(adventurer: Adventurer) -> None:
    """Tests a pre-defined adventurer."""
    assert adventurer.adventurer_id == "adv-001"
    assert adventurer.username == "Nox"
    assert adventurer.adventurer_class is AdventurerClass.WARRIOR
    assert adventurer.level == 1
    assert adventurer.status is AdventurerStatus.AVAILABLE


### ---------- Username Tests ---------- ###
def test_username_whitespace_only() -> None:
    """Tests that a ValueError is raised when a username is empty."""
    with pytest.raises(ValueError, match="Username cannot be empty"):
        Adventurer("adv-001", "   ", AdventurerClass.WARRIOR, 1)


def test_username_length_short() -> None:
    """Tests that a ValueError is raised when the username is too short."""
    with pytest.raises(
        ValueError,
        match="Username must be between 3 and 15 characters",
    ):
        Adventurer("adv-001", "No", AdventurerClass.WARRIOR, 1)


def test_username_length_long() -> None:
    """Tests that a ValueError is raised when the username is too long."""
    with pytest.raises(
        ValueError,
        match="Username must be between 3 and 15 characters",
    ):
        Adventurer("adv-001", "Noxtrum1234567890", AdventurerClass.WARRIOR, 1)


### ---------- Level Up Tests ---------- ###
def test_level_up(adventurer: Adventurer) -> None:
    """Tests that the adventurer levels up by 1."""
    adventurer.level_up()

    assert adventurer.level == 2


def test_level_low() -> None:
    """Tests that a ValueError triggers for an invalid level."""
    with pytest.raises(ValueError, match="Level must be greater than zero"):
        Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 0)


def test_level_up_while_retired(adventurer: Adventurer) -> None:
    """Tests that a retired adventurer cannot level up."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED

    with pytest.raises(
        ValueError,
        match="Retired adventurers cannot level up",
    ):
        adventurer.level_up()

    assert adventurer.level == 1


### ---------- Status Tests ---------- ###
def test_status_injured(adventurer: Adventurer) -> None:
    """Tests that an available adventurer becomes injured."""
    assert adventurer.status is AdventurerStatus.AVAILABLE

    adventurer.injured()

    assert adventurer.status is AdventurerStatus.INJURED


def test_status_recovered(adventurer: Adventurer) -> None:
    """Tests that an injured adventurer recovers."""
    adventurer.injured()

    assert adventurer.status is AdventurerStatus.INJURED

    adventurer.recover()

    assert adventurer.status is AdventurerStatus.AVAILABLE


def test_status_recover_invalid(adventurer: Adventurer) -> None:
    """Tests that a non-injured adventurer cannot recover."""
    with pytest.raises(
        ValueError,
        match="Only injured adventurers can recover",
    ):
        adventurer.recover()


def test_status_retired(adventurer: Adventurer) -> None:
    """Tests that an adventurer status updates to retired."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED


def test_status_retired_to_injured(adventurer: Adventurer) -> None:
    """Tests that a retired adventurer cannot become injured."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED

    with pytest.raises(
        ValueError,
        match="Retired adventurers cannot be injured",
    ):
        adventurer.injured()


def test_status_injured_to_injured(adventurer: Adventurer) -> None:
    """Tests that an already injured adventurer cannot become injured again."""
    adventurer.injured()

    assert adventurer.status is AdventurerStatus.INJURED

    with pytest.raises(
        ValueError,
        match="The adventurer is already injured",
    ):
        adventurer.injured()


def test_status_retired_to_retired(adventurer: Adventurer) -> None:
    """Tests that an already retired adventurer cannot retire again."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED

    with pytest.raises(
        ValueError,
        match="The adventurer is already retired",
    ):
        adventurer.retire()