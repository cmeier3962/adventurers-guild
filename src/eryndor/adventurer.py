from eryndor.enums import AdventurerStatus, EquipmentSlot, JobType
from eryndor.equipment import Equipment
from eryndor.inventory import Inventory
from eryndor.item import Item
from eryndor.progression import Progression
from eryndor.reward import Reward


class Adventurer:
    """Creates an adventurer object with identity, inventory, equipment, and progression."""

    def __init__(
        self,
        adventurer_id: str,
        username: str,
        job_type: JobType,
        inventory: Inventory | None = None,
    ) -> None:
        self.id = adventurer_id

        username_formatted = username.strip()
        if username_formatted == "":
            raise ValueError("Username cannot be empty.")
        if len(username_formatted) < 3 or len(username_formatted) > 15:
            raise ValueError("Username must be between 3 and 15 characters.")
        self.username = username_formatted

        self.job_type = job_type

        self.inventory = inventory if inventory is not None else Inventory()

        self.equipment = Equipment()

        self.unclaimed_items: list[Item] = []

        self.progression = Progression()

        self.status = AdventurerStatus.AVAILABLE

    @property
    def experience(self) -> int:
        """Returns current adventurer experience."""
        return self.progression.experience

    @property
    def level(self) -> int:
        """Returns current adventurer level."""
        return self.progression.level

    def gain_experience(self, amount: int) -> None:
        """Adds experience to the adventurer's progression."""
        self.progression.add_experience(amount)

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

    def receive_reward(self, reward: Reward) -> None:
        """Applies a reward and stores any unstored items as unclaimed."""
        self.progression.add_experience(reward.experience)

        for item in reward.items:
            if not self.receive_item(item):
                self.unclaimed_items.append(item)

    def claim_unclaimed_items(self) -> None:
        """Attempts to move unclaimed items into the adventurer's inventory."""
        remaining_items: list[Item] = []

        for item in self.unclaimed_items:
            if not self.receive_item(item):
                remaining_items.append(item)

        self.unclaimed_items = remaining_items

    def equip_item(self, item: Item) -> bool:
        """Attempts to equip an item and return an already equipped item to the inventory."""
        if item not in self.inventory.items:
            return False
        if item.slot is None:
            return False

        self.inventory.remove_item(item)

        unequipped_item = self.equipment.equip_item(item)

        if unequipped_item is not None:
            self.inventory.add_item(unequipped_item)

        return True

    def unequip_item(self, slot: EquipmentSlot) -> bool:
        """Attempts to unequip an item if an item is equipped in the slot and return it to the
        inventory."""
        if self.inventory.is_full:
            return False

        unequipped_item: Item | None = self.equipment.unequip_item(slot)

        if unequipped_item is None:
            return False

        return self.inventory.add_item(unequipped_item)
