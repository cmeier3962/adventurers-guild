from eryndor.enums import EquipmentSlot
from eryndor.item import Item


class Equipment:
    """Creates and manages an Adventurers equipment."""

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
