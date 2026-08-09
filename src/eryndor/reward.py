from eryndor.item import Item


class Reward:
    """Stores rewards granted from game activities."""
    
    def __init__(
        self,
        experience: int = 0,
        items: list[Item] | None = None,
    ) -> None:
        if experience < 0:
            raise ValueError("Experience reward must be >= 0.")
        self.experience = experience
        
        if items is None:
            self.items = []
        else:
            self.items = list(items)