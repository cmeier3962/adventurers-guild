import pytest

from eryndor.enums import ItemRarity, ItemType
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
        )
