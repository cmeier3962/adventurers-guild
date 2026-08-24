from eryndor.enums import EquipmentSlot, ItemRarity, ItemType
from eryndor.stats import Stats


class Item:
    """Represents an item that can be owned, equipped, consumed, or used."""

    def __init__(
        self,
        item_id: str,
        name: str,
        description: str,
        item_type: ItemType,
        rarity: ItemRarity,
        value: int,
        slot: EquipmentSlot | None = None,
        stats: Stats | None = None,
    ) -> None:
        self.id = item_id

        item_name = name.strip()
        if item_name == "":
            raise ValueError("Item name cannot be blank.")
        if len(item_name) < 3 or len(item_name) > 50:
            raise ValueError("Item name must be between 3 and 50 characters.")
        self.name = item_name

        item_description = description.strip()
        if item_description == "":
            raise ValueError("Item description cannot be blank.")
        if len(item_description) < 5:
            raise ValueError("Item description must be at least 5 characters.")
        self.description = item_description

        self.item_type = item_type

        self.rarity = rarity

        if value < 0:
            raise ValueError("Item value cannot be less than 0.")
        self.value = value

        if (
            self.item_type not in [ItemType.WEAPON, ItemType.ARMOR, ItemType.ACCESSORY]
            and slot is not None
        ):
            raise ValueError("Item cannot be equipped.")
        if self.item_type in [ItemType.WEAPON, ItemType.ARMOR, ItemType.ACCESSORY] and slot is None:
            raise ValueError("Item must be assigned to an equipment slot.")
        if self.item_type == ItemType.WEAPON and slot not in [
            EquipmentSlot.MAIN_HAND,
            EquipmentSlot.OFF_HAND,
        ]:
            raise ValueError("Item can only be equipped in a weapon slot.")
        if self.item_type == ItemType.ARMOR and slot not in [
            EquipmentSlot.HEAD,
            EquipmentSlot.CHEST,
            EquipmentSlot.HANDS,
            EquipmentSlot.LEGS,
            EquipmentSlot.FEET,
        ]:
            raise ValueError("Item can only be equipped in an armor slot.")
        if self.item_type == ItemType.ACCESSORY and slot not in [
            EquipmentSlot.BACK,
            EquipmentSlot.RING_1,
            EquipmentSlot.RING_2,
            EquipmentSlot.AMULET,
        ]:
            raise ValueError("Item can only be equipped in an accessory slot.")
        self.slot = slot

        self.stats = stats if stats is not None else Stats()
