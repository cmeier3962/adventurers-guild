import pytest

from eryndor.enums import ItemRarity, ItemType
from eryndor.inventory import Inventory
from eryndor.item import Item


### ---------- Initialization Tests ---------- ###
def test_inventory_initialization_with_default_capacity() -> None:
    """Tests the creation of a valid inventory object."""
    inventory = Inventory()
    assert inventory.capacity == 20
    assert inventory.items == []


def test_inventory_capacity_is_negative() -> None:
    """Tests that the inventory size cannot be less than 1."""
    with pytest.raises(ValueError, match="Capacity cannot be less than 1"):
        Inventory(-5)


def test_inventory_item_count_zero() -> None:
    """Tests that the inventory item count can be zero."""
    inventory = Inventory()
    assert inventory.item_count == 0


def test_inventory_available_slots() -> None:
    """Tests the number of inventory slots available are accurate."""
    inventory = Inventory()
    assert inventory.available_slots == 20


def test_inventory_is_full() -> None:
    """Tests whether the inventory is full."""
    inventory = Inventory()
    assert not inventory.is_full


### ---------- Tests to Add Items ---------- ###
def test_add_item_success(item: Item) -> None:
    """Validations item is added to inventory."""
    inventory = Inventory()
    assert inventory.add_item(item)

    assert inventory.item_count == 1
    assert item in inventory.items


def test_add_item_failed_inventory_full(item: Item) -> None:
    """Tests that item is not added to inventory when full."""
    inventory = Inventory(1)
    inventory.add_item(item)
    assert inventory.item_count == 1
    assert inventory.available_slots == 0

    assert not inventory.add_item(item)

    assert inventory.item_count == 1


### ---------- Tests to Remove Items ---------- ###
def test_remove_item_success(item: Item) -> None:
    """Validates item is removed from inventory."""
    inventory = Inventory()
    inventory.add_item(item)
    assert item in inventory.items

    assert inventory.remove_item(item)

    assert item not in inventory.items


def test_remove_item_failure_when_item_not_found(item: Item) -> None:
    """Tests that an item cannot be removed from the inventory that doesn't exist."""
    inventory = Inventory()
    assert inventory.item_count == 0
    assert item not in inventory.items

    assert not inventory.remove_item(item)

    assert inventory.item_count == 0


def test_remove_item_failure_when_item_not_found_in_non_empty_inventory(item: Item) -> None:
    """Tests that a item doesn't exist in a non-empty inventory."""
    inventory = Inventory()
    inventory.add_item(item)
    assert inventory.item_count == 1
    assert item in inventory.items

    item2 = Item(
        "item-002",
        "Beginner Sword",
        "A farily dull sword but will get the job done.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        20,
    )
    assert item2 not in inventory.items

    assert not inventory.remove_item(item2)

    assert inventory.item_count == 1
    assert item in inventory.items
