from math import floor, sqrt


class Progression:
    """Tracks and manages an adventurers experience."""

    def __init__(self, experience: int = 0) -> None:
        if experience < 0:
            raise ValueError("Starting experience cannot be less than zero.")
        self.experience = experience

    @property
    def level(self) -> int:
        """Calculates and returns level based on experience."""
        return floor(sqrt(self.experience / 100)) + 1

    def add_experience(self, amount: int) -> None:
        """Adds experience to current progression objects experience."""
        if amount < 0:
            raise ValueError("Added experience cannot be negative.")

        self.experience += amount
