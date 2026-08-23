from eryndor.enums import EquipmentSlot, StatType
from eryndor.item import Item


class Equipment:
    """Creates and manages an adventurer's equipment."""

    def __init__(self) -> None:
        self.slots: dict[EquipmentSlot, Item | None] = {
            EquipmentSlot.HEAD: None,
            EquipmentSlot.CHEST: None,
            EquipmentSlot.HANDS: None,
            EquipmentSlot.LEGS: None,
            EquipmentSlot.FEET: None,
            EquipmentSlot.BACK: None,
            EquipmentSlot.RING_1: None,
            EquipmentSlot.RING_2: None,
            EquipmentSlot.AMULET: None,
            EquipmentSlot.MAIN_HAND: None,
            EquipmentSlot.OFF_HAND: None,
        }

    def equip_item(self, item: Item) -> Item | None:
        """Checks an items slot and equips it if the slot is empty."""
        if item.slot is None:
            raise ValueError("The item is not equippable.")

        unequip_item: Item | None = None

        if self.slots[item.slot] is not None:
            unequip_item = self.slots[item.slot]

        self.slots[item.slot] = item
        return unequip_item

    def unequip_item(self, slot: EquipmentSlot) -> Item | None:
        """Unequips an item in a slot if it is filled and returns the item."""
        if self.slots[slot] is None:
            return None

        unequip_item: Item | None = self.slots[slot]

        self.slots[slot] = None
        return unequip_item

    def get_item(self, slot: EquipmentSlot) -> Item | None:
        """Returns the item currently equipped in the specified slot."""
        return self.slots[slot]

    def is_slot_occupied(self, slot: EquipmentSlot) -> bool:
        """Checks to see if a slot has an equipped item."""
        return self.slots[slot] is not None

    def get_total_stats(self) -> dict[StatType, int]:
        """Returns the sum of all stats of equipped items."""
        stat_totals: dict[StatType, int] = {}

        for item in self.slots.values():
            if item is not None:
                for stat, value in item.stats.items():
                    if stat not in stat_totals:
                        stat_totals[stat] = 0

                    stat_totals[stat] += value

        return stat_totals
