import pytest

from eryndor.progression import Progression


### ---------- Initialize Class Tests ---------- ###
def test_progression_initialization_default_exp() -> None:
    """Tests the creation of a default progression object."""
    progress = Progression()
    assert progress.experience == 0
    assert progress.level == 1


def test_progression_initialization_custom_exp() -> None:
    """Tests the creation of a progression object with a custom experience amount."""
    progress = Progression(1000)
    assert progress.experience == 1000
    assert progress.level == 4


def test_progression_initialization_negative_exp() -> None:
    """Tests that the creation of a progression object with negative experience fails."""
    with pytest.raises(ValueError, match="Starting experience cannot be less than zero"):
        Progression(-10)


### ---------- Experience Tests ---------- ###
def test_add_experience() -> None:
    """Tests that experience is successfully added to currently stored experience."""
    progress = Progression()
    assert progress.experience == 0

    progress.add_experience(100)
    assert progress.experience == 100


def test_add_negative_experience() -> None:
    """Tests that negative experience raises an error."""
    progress = Progression()
    assert progress.experience == 0

    with pytest.raises(ValueError, match="Added experience cannot be negative"):
        progress.add_experience(-100)

    assert progress.experience == 0


### ---------- Level Tests ---------- ###
def test_level_default() -> None:
    """Tests the level calculation from the currently stored experience."""
    progress = Progression()
    assert progress.level == 1


def test_level_boundaries() -> None:
    """Tests the level calculation for experience nearing a new level."""
    progress = Progression(99)
    assert progress.level == 1

    progress.add_experience(1)
    assert progress.experience == 100
    assert progress.level == 2

    progress.add_experience(299)
    assert progress.experience == 399
    assert progress.level == 2

    progress.add_experience(1)
    assert progress.experience == 400
    assert progress.level == 3
