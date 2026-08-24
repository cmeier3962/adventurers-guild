import pytest

from eryndor.stats import Stats, StatType


### ---------- Initialization Tests ---------- ###
def test_stats_initialization_empty() -> None:
    """Tests that stats initialize with an empty dictionary by default."""
    stats = Stats()

    assert stats.values == {}


def test_stats_initialization_with_values() -> None:
    """Tests that stats initialize with provided values."""
    stats = Stats(
        {
            StatType.ATTACK: 10,
            StatType.DEFENSE: 5,
        }
    )

    assert stats.values == {
        StatType.ATTACK: 10,
        StatType.DEFENSE: 5,
    }


def test_stats_values_are_independent_from_original_dictionary() -> None:
    """Tests that stats do not share the original dictionary reference."""
    values = {
        StatType.ATTACK: 10,
    }

    stats = Stats(values)

    values[StatType.ATTACK] = 50

    assert stats.get_stat(StatType.ATTACK) == 10


### ---------- Validation Tests ---------- ###
def test_stats_negative_values_are_invalid() -> None:
    """Tests that stats cannot be initialized with negative values."""
    with pytest.raises(ValueError, match="Stats cannot contain negative values."):
        Stats(
            {
                StatType.ATTACK: -1,
            }
        )


### ---------- Get stat Tests ---------- ###
@pytest.mark.parametrize(
    "stat_type",
    [
        StatType.ATTACK,
        StatType.DEFENSE,
        StatType.HEALTH,
    ],
)
def test_get_stat_missing_stat_returns_zero(stat_type: StatType) -> None:
    """Tests that missing stats return zero."""
    stats = Stats()

    assert stats.get_stat(stat_type) == 0


def test_get_stat_existing_stat_returns_value() -> None:
    """Tests that existing stats return their stored value."""
    stats = Stats(
        {
            StatType.ATTACK: 10,
        }
    )

    assert stats.get_stat(StatType.ATTACK) == 10


### ---------- Add Stat Tests ---------- ###
def test_add_stat_new_stat() -> None:
    """Tests that adding a new stat stores the value."""
    stats = Stats()

    stats.add_stat(StatType.ATTACK, 10)

    assert stats.get_stat(StatType.ATTACK) == 10


def test_add_stat_existing_stat() -> None:
    """Tests that adding to an existing stat increases the value."""
    stats = Stats(
        {
            StatType.ATTACK: 10,
        }
    )

    stats.add_stat(StatType.ATTACK, 5)

    assert stats.get_stat(StatType.ATTACK) == 15


def test_add_stat_negative_value_is_invalid() -> None:
    """Tests that stats cannot be increased by a negative value."""
    stats = Stats()

    with pytest.raises(ValueError, match="Stats cannot contain negative values."):
        stats.add_stat(StatType.ATTACK, -5)


def test_stats_add_stat_does_not_modify_other_stats() -> None:
    """Tests adding a stat does not modify unrelated stats."""
    stats = Stats(
        {
            StatType.DEFENSE: 10,
        }
    )

    stats.add_stat(
        StatType.ATTACK,
        5,
    )

    assert stats.get_stat(StatType.DEFENSE) == 10
    assert stats.get_stat(StatType.ATTACK) == 5
