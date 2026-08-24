from enum import StrEnum


class StatType(StrEnum):
    """Available statistics used throughout Eryndor."""

    HEALTH = "Health"
    ATTACK = "Attack"
    DEFENSE = "Defense"


class Stats:
    """Stores and manages a collection of statistics."""

    def __init__(
        self,
        values: dict[StatType, int] | None = None,
    ) -> None:
        if values is None:
            self.values: dict[StatType, int] = {}
        else:
            for value in values.values():
                if value < 0:
                    raise ValueError("Stats cannot contain negative values.")

            self.values = dict(values)

    def get_stat(self, stat_type: StatType) -> int:
        """Returns a stat value or zero if it does not exist."""
        return self.values.get(stat_type, 0)

    def add_stat(self, stat_type: StatType, value: int) -> None:
        """Adds to an existing stat value."""
        if value < 0:
            raise ValueError("Stats cannot contain negative values.")

        self.values[stat_type] = self.get_stat(stat_type) + value
