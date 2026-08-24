import pytest

from eryndor.adventurer import Adventurer
from eryndor.enums import AdventurerClass, EquipmentSlot, ItemRarity, ItemType
from eryndor.item import Item
from eryndor.party import Party
from eryndor.reward import Reward
from eryndor.stats import Stats, StatType


@pytest.fixture
def adventurer() -> Adventurer:
    """Returns a valid adventurer."""
    return Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR)


@pytest.fixture
def item() -> Item:
    """Returns a valid item."""
    return Item(
        "item-001",
        "Novice Sword",
        "A basic sword.",
        ItemType.WEAPON,
        ItemRarity.COMMON,
        10,
        EquipmentSlot.MAIN_HAND,
        Stats(
            {
                StatType.ATTACK: 5,
            },
        ),
    )


@pytest.fixture
def reward_with_item(item: Item) -> Reward:
    """Returns a valid reward containing experience and an item."""
    return Reward(100, [item])


@pytest.fixture
def empty_party() -> Party:
    """Returns an empty party."""
    return Party("12345", "Nox's Party")


@pytest.fixture
def party(adventurer: Adventurer) -> Party:
    """Returns a valid party with one member and a leader."""
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.assign_leader(adventurer)
    return party


@pytest.fixture
def party_without_leader(adventurer: Adventurer) -> Party:
    """Returns a party with a member but no leader."""
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    return party
