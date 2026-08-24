import pytest

from eryndor.adventurer import Adventurer
from eryndor.enums import AdventurerStatus, EquipmentSlot, ItemRarity, ItemType, JobType
from eryndor.equipment import Equipment
from eryndor.inventory import Inventory
from eryndor.item import Item
from eryndor.progression import Progression
from eryndor.reward import Reward


### ---------- Fixtures ---------- ###
@pytest.fixture
def adventurer() -> Adventurer:
    """Returns a valid available adventurer."""
    return Adventurer("adv-001", "Nox", JobType.MARTIALIST)


@pytest.fixture
def one_slot_inventory() -> Inventory:
    """Returns a custom inventory of 1."""
    return Inventory(1)


### ---------- Initialize Class Tests ---------- ###
def test_adventurer_initialization(adventurer: Adventurer) -> None:
    """Tests a pre-defined adventurer."""
    assert adventurer.id == "adv-001"
    assert adventurer.username == "Nox"
    assert adventurer.job_type is JobType.MARTIALIST
    assert isinstance(adventurer.inventory, Inventory)
    assert isinstance(adventurer.equipment, Equipment)
    assert isinstance(adventurer.progression, Progression)
    assert adventurer.experience == 0
    assert adventurer.level == 1
    assert adventurer.status is AdventurerStatus.AVAILABLE


def test_adventurer_with_custom_inventory(one_slot_inventory: Inventory) -> None:
    """Tests the creation of an adventurer with a custom inventory capacity."""
    adventurer = Adventurer("adv-001", "Nox", JobType.MARTIALIST, one_slot_inventory)
    assert adventurer.inventory is one_slot_inventory
    assert adventurer.inventory.capacity == 1


def test_adventurer_with_inventory_as_none() -> None:
    """Tests the creation of an adventurer with no inventory provided."""
    adventurer = Adventurer("adv-001", "Nox", JobType.MARTIALIST, None)
    assert isinstance(adventurer.inventory, Inventory)


def test_adventurers_with_separate_inventories(adventurer: Adventurer, item: Item) -> None:
    """Tests the creation of 2 adventurers and verifies their inventories are separate."""
    adventurer2 = Adventurer("adv-002", "Box", JobType.MARTIALIST)
    assert adventurer2.inventory.item_count == 0

    assert adventurer.inventory is not adventurer2.inventory

    adventurer.inventory.add_item(item)
    assert adventurer.inventory.item_count == 1

    assert adventurer2.inventory.item_count == 0


def test_adventurers_with_separate_progressions(adventurer: Adventurer) -> None:
    """Tests the creation of 2 adventurers and verifies their progressions are separate."""
    adventurer2 = Adventurer("adv-002", "Box", JobType.MARTIALIST)

    assert adventurer.progression is not adventurer2.progression


### ---------- Username Tests ---------- ###
def test_username_whitespace_only() -> None:
    """Tests that a ValueError is raised when a username is empty."""
    with pytest.raises(ValueError, match="Username cannot be empty"):
        Adventurer("adv-001", "   ", JobType.MARTIALIST)


def test_username_length_short() -> None:
    """Tests that a ValueError is raised when the username is too short."""
    with pytest.raises(
        ValueError,
        match="Username must be between 3 and 15 characters",
    ):
        Adventurer("adv-001", "No", JobType.MARTIALIST)


def test_username_length_long() -> None:
    """Tests that a ValueError is raised when the username is too long."""
    with pytest.raises(
        ValueError,
        match="Username must be between 3 and 15 characters",
    ):
        Adventurer("adv-001", "Noxtrum1234567890", JobType.MARTIALIST)


### ---------- Status Tests ---------- ###
def test_status_injured(adventurer: Adventurer) -> None:
    """Tests that an available adventurer becomes injured."""
    assert adventurer.status is AdventurerStatus.AVAILABLE

    adventurer.injured()

    assert adventurer.status is AdventurerStatus.INJURED


def test_status_recovered(adventurer: Adventurer) -> None:
    """Tests that an injured adventurer recovers."""
    adventurer.injured()

    assert adventurer.status is AdventurerStatus.INJURED

    adventurer.recover()

    assert adventurer.status is AdventurerStatus.AVAILABLE


def test_status_recover_invalid(adventurer: Adventurer) -> None:
    """Tests that a non-injured adventurer cannot recover."""
    with pytest.raises(
        ValueError,
        match="Only injured adventurers can recover",
    ):
        adventurer.recover()


def test_status_retired(adventurer: Adventurer) -> None:
    """Tests that an adventurer status updates to retired."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED


def test_status_retired_to_injured(adventurer: Adventurer) -> None:
    """Tests that a retired adventurer cannot become injured."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED

    with pytest.raises(
        ValueError,
        match="Retired adventurers cannot be injured",
    ):
        adventurer.injured()


def test_status_injured_to_injured(adventurer: Adventurer) -> None:
    """Tests that an already injured adventurer cannot become injured again."""
    adventurer.injured()

    assert adventurer.status is AdventurerStatus.INJURED

    with pytest.raises(
        ValueError,
        match="The adventurer is already injured",
    ):
        adventurer.injured()


def test_status_retired_to_retired(adventurer: Adventurer) -> None:
    """Tests that an already retired adventurer cannot retire again."""
    adventurer.retire()

    assert adventurer.status is AdventurerStatus.RETIRED

    with pytest.raises(
        ValueError,
        match="The adventurer is already retired",
    ):
        adventurer.retire()


### ---------- Inventory Tests ---------- ###
def test_receive_item_successfully(adventurer: Adventurer, item: Item) -> None:
    """Tests that an adventurer receives an item and stores it in their inventory."""
    assert adventurer.receive_item(item)

    assert item in adventurer.inventory.items


def test_receive_item_inventory_full(
    adventurer: Adventurer, one_slot_inventory: Inventory, item: Item
) -> None:
    """Tests that receive item fails when inventory is full."""
    adventurer = Adventurer("adv-001", "Nox", JobType.MARTIALIST, one_slot_inventory)

    assert adventurer.receive_item(item)

    assert adventurer.inventory.is_full

    assert not adventurer.receive_item(item)

    assert adventurer.inventory.available_slots == 0
    assert adventurer.inventory.item_count == 1


### ---------- Experience/Level Tests ---------- ###
def test_gain_experience(adventurer: Adventurer) -> None:
    """Tests to add experience to adventurer's progression."""
    assert adventurer.experience == 0

    adventurer.gain_experience(100)

    assert adventurer.experience == 100


### ---------- Rewards Tests ---------- ###
def test_receive_reward_exp_and_items_no_unclaimed_items(
    adventurer: Adventurer, reward_with_item: Reward
) -> None:
    """Tests that the adventurer successfully receives both the exp and item from receive
    rewards."""
    adventurer.receive_reward(reward_with_item)

    assert adventurer.experience == 100
    assert adventurer.inventory.item_count == 1
    assert adventurer.unclaimed_items == []


def test_receive_reward_with_full_inventory(
    one_slot_inventory: Inventory, item: Item, reward_with_item: Reward
) -> None:
    """Tests that the adventurer receives the exp and stores unstored reward items as unclaimed."""
    adventurer = Adventurer("adv-001", "Nox", JobType.MARTIALIST, one_slot_inventory)

    adventurer.receive_item(item)
    assert adventurer.inventory.is_full

    adventurer.receive_reward(reward_with_item)
    assert adventurer.unclaimed_items == reward_with_item.items
    assert adventurer.experience == 100
    assert item in adventurer.inventory.items
    assert adventurer.inventory.item_count == 1


def test_claim_unclaimed_items(adventurer: Adventurer, item: Item) -> None:
    """Tests to verify that unclaimed items successfully move to the adventurers inventory."""
    adventurer.unclaimed_items.append(item)
    assert adventurer.unclaimed_items == [item]

    adventurer.claim_unclaimed_items()
    assert item in adventurer.inventory.items
    assert adventurer.unclaimed_items == []


def test_claim_unclaimed_items_with_full_inventory(
    one_slot_inventory: Inventory, item: Item
) -> None:
    """Tests that items that don't fit in the inventory remain in unclaimed items."""
    adventurer = Adventurer("adv-001", "Nox", JobType.MARTIALIST, one_slot_inventory)

    adventurer.receive_item(item)
    assert adventurer.inventory.item_count == 1

    adventurer.unclaimed_items.append(item)
    assert len(adventurer.unclaimed_items) == 1

    adventurer.claim_unclaimed_items()
    assert adventurer.inventory.item_count == 1
    assert len(adventurer.unclaimed_items) == 1


### ---------- Equip Item Tests ---------- ###
def test_equip_item_to_empty_slot(adventurer: Adventurer, item: Item) -> None:
    """Test to equip an item to an empty slot"""
    adventurer.receive_item(item)
    assert item in adventurer.inventory.items
    assert item.slot is not None

    assert adventurer.equip_item(item)
    assert adventurer.equipment.slots[item.slot] == item
    assert item not in adventurer.inventory.items


def test_equip_item_to_occupied_slot(adventurer: Adventurer, item: Item) -> None:
    """Test to equip an item in a preoccupied slot and return the item to the inventory."""
    adventurer.receive_item(item)
    assert item.slot is not None
    assert adventurer.equip_item(item)

    item_2 = Item(
        "Item-002",
        "Test Sword",
        "A test sword.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        10,
        EquipmentSlot.MAIN_HAND,
    )
    assert adventurer.receive_item(item_2)
    assert item_2.slot is not None

    assert adventurer.equip_item(item_2)
    assert adventurer.equipment.slots[item_2.slot] == item_2
    assert item in adventurer.inventory.items
    assert item_2 not in adventurer.inventory.items


def test_equip_item_not_in_inventory(adventurer: Adventurer, item: Item) -> None:
    """Test to fail to equip an item not in inventory."""
    assert item not in adventurer.inventory.items
    assert not adventurer.equip_item(item)


def test_equip_non_equippable_item(adventurer: Adventurer) -> None:
    """Test to fail to equip a non equippable item."""
    item_2 = Item(
        "Item-002", "Test Sword", "A test sword.", ItemType.CONSUMABLE, ItemRarity.COMMON, 10, None
    )
    adventurer.receive_item(item_2)
    assert not adventurer.equip_item(item_2)


def test_unequip_item_with_full_inventory(item: Item, one_slot_inventory: Inventory) -> None:
    """Tests to fail to unequip an item due to full inventory."""
    adventurer = Adventurer("adv-001", "Nox", JobType.MARTIALIST, one_slot_inventory)
    adventurer.receive_item(item)
    adventurer.equip_item(item)
    assert adventurer.equipment.slots[EquipmentSlot.MAIN_HAND] is item

    item_2 = Item(
        "Item-002", "Test Sword", "A test sword.", ItemType.CONSUMABLE, ItemRarity.COMMON, 10, None
    )
    adventurer.receive_item(item_2)

    assert not adventurer.unequip_item(EquipmentSlot.MAIN_HAND)
    assert adventurer.equipment.slots[EquipmentSlot.MAIN_HAND] is item


def test_unequip_item_on_empty_slot(adventurer: Adventurer) -> None:
    """Tests to fail unequipping an item slot that has no item."""
    assert adventurer.equipment.slots[EquipmentSlot.MAIN_HAND] is None
    assert not adventurer.unequip_item(EquipmentSlot.MAIN_HAND)


def test_unequip_item_successfully(adventurer: Adventurer, item: Item) -> None:
    """Tests that unequipping an item returns the item to the inventory."""
    adventurer.receive_item(item)
    adventurer.equip_item(item)
    assert adventurer.equipment.slots[EquipmentSlot.MAIN_HAND] is item
    assert not adventurer.inventory.is_full

    assert adventurer.unequip_item(EquipmentSlot.MAIN_HAND)
    assert adventurer.equipment.slots[EquipmentSlot.MAIN_HAND] is None
    assert item in adventurer.inventory.items
