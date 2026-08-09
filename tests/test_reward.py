import pytest

from eryndor.item import Item
from eryndor.reward import Reward


### ---------- Initialization Tests ---------- ###
def test_reward_initialization_default() -> None:
    """Tests the creation of a default reward object."""
    reward = Reward()
    assert reward.experience == 0
    assert reward.items == []


def test_reward_initialization_custom_exp_only() -> None:
    """Tests the creation of a custom reward object that only contains an experience reward."""
    reward = Reward(experience=100)
    assert reward.experience == 100
    assert reward.items == []


def test_reward_initialization_custom_items_only(item: Item) -> None:
    """Tests the creation of a custom reward object that only contains an item(s) reward."""
    reward = Reward(items=[item])
    assert reward.experience == 0
    assert item in reward.items


def test_reward_initialization_custom_exp_and_items(item: Item, reward_with_item: Reward) -> None:
    """Tests the creation of a custom reward object."""
    assert reward_with_item.experience == 100
    assert item in reward_with_item.items


def test_reward_initialization_negative_experience() -> None:
    """Tests a reward object's experience cannot be negative."""
    with pytest.raises(ValueError, match="Experience reward must be >= 0"):
        Reward(-100)


def test_reward_items_are_independent_from_original_list(item: Item) -> None:
    """Tests that reward stores its own copy of the item list."""
    items = [item]
    reward = Reward(items=items)

    items.clear()

    assert item in reward.items