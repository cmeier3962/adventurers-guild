from eryndor.item import Item


class Inventory:
    """Stores and manages items owned by an adventurer."""

    def __init__(self, capacity: int = 20) -> None:
        if capacity < 1:
            raise ValueError("Capacity cannot be less than 1.")
        self.capacity = capacity

        self.items: list[Item] = []

    @property
    def item_count(self) -> int:
        """Returns the number of items in the inventory."""
        return len(self.items)

    @property
    def available_slots(self) -> int:
        """Returns the number of available inventory slots left."""
        return self.capacity - self.item_count

    @property
    def is_full(self) -> bool:
        """Returns a boolean whether or not the inventory is full."""
        return self.available_slots == 0

    def add_item(self, item: Item) -> bool:
        """Adds an item to the inventory if space is available."""
        if self.is_full:
            return False

        self.items.append(item)
        return True

    def remove_item(self, item: Item) -> bool:
        """Removes an item from the inventory if it exists."""
        for i in self.items:
            if i.id == item.id:
                self.items.remove(i)
                return True

        return False
