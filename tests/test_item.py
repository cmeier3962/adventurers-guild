import pytest

from eryndor.enums import ItemRarity, ItemType, EquipmentSlot, StatType
from eryndor.item import Item


### ---------- Initialize Class Tests ---------- ###
def test_item(item: Item) -> None:
    """Tests the creation of a valid item object."""
    assert item.id == "item-001"
    assert item.name == "Novice Sword"
    assert item.description == "A basic sword."
    assert item.item_type is ItemType.WEAPON
    assert item.rarity is ItemRarity.COMMON
    assert item.value == 10
    assert item.slot is EquipmentSlot.MAIN_HAND
    assert item.stats[StatType.ATTACK] == 5


### ---------- Item Name Tests ---------- ###
def test_item_name_whitespace_only() -> None:
    """Tests that an item's name cannot contain only whitespaces."""
    with pytest.raises(ValueError, match="Item name cannot be blank"):
        Item(
            "item-001",
            "     ",
            "A basic sword.",
            ItemType.WEAPON,
            ItemRarity.COMMON,
            10,
            EquipmentSlot.MAIN_HAND,
        )


def test_item_name_whitespace_before_and_after() -> None:
    """Tests that an item's name with whitespaces before and after are removed."""
    item = Item(
        "item-001",
        "     Novice Sword     ",
        "A basic sword.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        10,
        EquipmentSlot.MAIN_HAND,
    )

    assert item.name == "Novice Sword"


def test_item_name_length_short() -> None:
    """Tests that an item's name cannot be less than 3 characters."""
    with pytest.raises(ValueError, match="Item name must be between 3 and 50 characters"):
        Item(
            "item-001",
            "A" * 2,
            "A basic sword.",
            ItemType.WEAPON,
            ItemRarity.COMMON,
            10,
            EquipmentSlot.MAIN_HAND,
        )


def test_item_name_length_long() -> None:
    """Tests that an item's name cannot be more than 50 characters."""
    with pytest.raises(ValueError, match="Item name must be between 3 and 50 characters"):
        Item(
            "item-001",
            "A" * 51,
            "A basic sword.",
            ItemType.WEAPON,
            ItemRarity.COMMON,
            10,
            EquipmentSlot.MAIN_HAND,
        )


### ---------- Item Description Tests ---------- ###
def test_item_description_whitespace_only() -> None:
    """Tests that an item's description cannot contain only whitespaces."""
    with pytest.raises(ValueError, match="Item description cannot be blank"):
        Item(
            "item-001",
            "Novice Sword",
            "     ",
            ItemType.WEAPON,
            ItemRarity.COMMON,
            10,
            EquipmentSlot.MAIN_HAND,
        )


def test_item_description_whitespace_before_and_after() -> None:
    """Tests that an item's description with whitespaces before and after are removed."""
    item = Item(
        "item-001",
        "Novice Sword",
        "     A basic sword.     ",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        10,
        EquipmentSlot.MAIN_HAND,
    )

    assert item.description == "A basic sword."


def test_item_description_length_short() -> None:
    """Tests that an item's description length cannot be less than 5 characters."""
    with pytest.raises(ValueError, match="Item description must be at least 5 characters"):
        Item(
            "item-001",
            "Novice Sword",
            "A" * 4,
            ItemType.WEAPON,
            ItemRarity.COMMON,
            10,
            EquipmentSlot.MAIN_HAND,
        )


### ---------- Item Value Tests ---------- ###
def test_item_value_zero() -> None:
    """Tests that an item's value can be zero."""
    item = Item(
        "item-001",
        "Novice Sword",
        "A basic sword.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        0,
        EquipmentSlot.MAIN_HAND,
    )

    assert item.value == 0


def test_item_value_below_zero() -> None:
    """Tests that an item's value cannot be negative."""
    with pytest.raises(ValueError, match="Item value cannot be less than 0"):
        Item(
            "item-001",
            "Novice Sword",
            "A basic sword.",
            ItemType.WEAPON,
            ItemRarity.COMMON,
            -100,
            EquipmentSlot.MAIN_HAND,
        )


### ---------- Item Type and Slot Tests ---------- ###
@pytest.mark.parametrize(
    ("item_type", "slot"),
    [
        (ItemType.WEAPON, EquipmentSlot.MAIN_HAND),
        (ItemType.ARMOR, EquipmentSlot.CHEST),
        (ItemType.ACCESSORY, EquipmentSlot.RING_1),
    ],
)
def test_item_valid_equipment_slots(
    item_type: ItemType,
    slot: EquipmentSlot,
) -> None:
    """Tests valid item type and slot combinations."""
    item = Item(
        "item-001",
        "Test Item",
        "A test item.",
        item_type,
        ItemRarity.COMMON,
        10,
        slot,
    )

    assert item.item_type is item_type
    assert item.slot is slot


@pytest.mark.parametrize(
    ("item_type", "slot", "error_message"),
    [
        (ItemType.CONSUMABLE, EquipmentSlot.MAIN_HAND, "Item cannot be equipped."),
        (ItemType.WEAPON, None, "Item must be assigned to an equipment slot."),
        (ItemType.WEAPON, EquipmentSlot.HEAD, "Item can only be equipped in a weapon slot."),
        (ItemType.ARMOR, EquipmentSlot.MAIN_HAND, "Item can only be equipped in an armor slot."),
        (
            ItemType.ACCESSORY,
            EquipmentSlot.MAIN_HAND,
            "Item can only be equipped in an accessory slot",
        ),
    ],
)
def test_item_invalid_equipment_slots(
    item_type: ItemType,
    slot: EquipmentSlot,
    error_message: str,
) -> None:
    """Tests invalid item type and slot combinations."""
    with pytest.raises(ValueError, match=error_message):
        Item(
            "item-001",
            "Test Item",
            "A test item.",
            item_type,
            ItemRarity.COMMON,
            10,
            slot,
        )


@pytest.mark.parametrize(
    "stat_type",
    [
        StatType.ATTACK,
        StatType.DEFENSE,
        StatType.HEALTH,
    ],
)
def test_negative_stat_type_values(stat_type: StatType) -> None:
    """Tests invalid values for different stat types."""
    with pytest.raises(ValueError, match="Item stats cannot be negative."):
        Item(
            "item-001",
            "Novice Sword",
            "A basic sword.",
            ItemType.WEAPON,
            ItemRarity.COMMON,
            10,
            EquipmentSlot.MAIN_HAND,
            {
                stat_type: -1,
            },
        )
