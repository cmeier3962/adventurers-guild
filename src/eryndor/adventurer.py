from eryndor.enums import AdventurerClass, AdventurerStatus
from eryndor.item import Item
from eryndor.inventory import Inventory


class Adventurer:
    """Creates an adventurer object with basic character information and statistics."""

    def __init__(
        self,
        adventurer_id: str,
        username: str,
        adventurer_class: AdventurerClass,
        level: int,
        inventory: Inventory | None = None,
    ) -> None:
        self.id = adventurer_id

        username_formatted = username.strip()
        if username_formatted == "":
            raise ValueError("Username cannot be empty.")
        if len(username_formatted) < 3 or len(username_formatted) > 15:
            raise ValueError("Username must be between 3 and 15 characters.")
        self.username = username_formatted

        self.adventurer_class = adventurer_class

        if level < 1:
            raise ValueError("Level must be greater than zero.")
        self.level = level

        self.status = AdventurerStatus.AVAILABLE
        
        if inventory is None:
            self.inventory = Inventory()
        else:
            self.inventory = inventory


    def level_up(self) -> None:
        """Increases adventurer's level by 1."""
        if self.status == AdventurerStatus.RETIRED:
            raise ValueError("Retired adventurers cannot level up.")

        self.level += 1


    def injured(self) -> None:
        """Updates the adventurer's status to injured."""
        if self.status == AdventurerStatus.RETIRED:
            raise ValueError("Retired adventurers cannot be injured.")

        if self.status == AdventurerStatus.INJURED:
            raise ValueError("The adventurer is already injured.")

        self.status = AdventurerStatus.INJURED


    def recover(self) -> None:
        """Updates adventurer's status to available."""
        if self.status != AdventurerStatus.INJURED:
            raise ValueError("Only injured adventurers can recover.")
        self.status = AdventurerStatus.AVAILABLE


    def retire(self) -> None:
        """Updates adventurer's status to retired."""
        if self.status == AdventurerStatus.RETIRED:
            raise ValueError("The adventurer is already retired.")

        self.status = AdventurerStatus.RETIRED

    
    def receive_item(self, item: Item) -> bool:
        """Attempts to receive an item and store it in adventurers inventory."""
        return self.inventory.add_item(item)