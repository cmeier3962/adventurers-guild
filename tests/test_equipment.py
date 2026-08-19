import pytest

from eryndor.enums import EquipmentSlot, ItemRarity, ItemType
from eryndor.equipment import Equipment
from eryndor.item import Item


### ---------- Initialization Tests ---------- ###
def test_equipment_initialization() -> None:
    """Tests that all equipment slots are created and empty."""
    equipment = Equipment()

    assert set(equipment.slots) == set(EquipmentSlot)
    assert all(item is None for item in equipment.slots.values())


### ---------- Equip Item Tests ---------- ###
def test_equip_item_to_empty_slot() -> None:
    """Tests equipping an item into an empty equipment slot."""
    equipment = Equipment()
    item = Item(
        "item-001",
        "Test Sword",
        "A test sword.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        10,
        EquipmentSlot.MAIN_HAND,
    )

    unequipped_item = equipment.equip_item(item)

    assert item.slot is not None
    assert equipment.slots[item.slot] is item
    assert unequipped_item is None


def test_equip_item_to_occupied_slot() -> None:
    """Tests replacing an equipped item and returning the previous item."""
    equipment = Equipment()

    item = Item(
        "item-001",
        "Old Sword",
        "An old sword.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        10,
        EquipmentSlot.MAIN_HAND,
    )
    item_2 = Item(
        "item-002",
        "New Sword",
        "A new sword.",
        ItemType.WEAPON,
        ItemRarity.UNCOMMON,
        20,
        EquipmentSlot.MAIN_HAND,
    )

    equipment.equip_item(item)
    unequipped_item = equipment.equip_item(item_2)

    assert item_2.slot is not None
    assert equipment.slots[item_2.slot] is item_2
    assert unequipped_item is item


def test_equip_non_equippable_item() -> None:
    """Tests that attempting to equip a non-equippable item raises an error."""
    equipment = Equipment()
    item = Item(
        "item-001",
        "Health Potion",
        "Restores health.",
        ItemType.CONSUMABLE,
        ItemRarity.COMMON,
        10,
    )

    with pytest.raises(ValueError, match="The item is not equippable."):
        equipment.equip_item(item)
