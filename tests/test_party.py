import pytest

from adventurers_guild.party import Party
from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, AdventurerStatus


### ---------- Initialize Class Tests---------- ###
def test_party() -> None:
    """Tests a predefined party."""
    party = Party("12345", "Nox's Party")
    assert party.party_id == "12345"
    assert party.name == "Nox's Party"
    assert party.members == []


### ---------- Add to Party Tests ---------- ###
def test_add_member() -> None:
    """Tests adding an adventurer to the party."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    assert adventurer in party.members
    assert adventurer.status == AdventurerStatus.ASSIGNED


def test_add_member_duplicate() -> None:
    """Tests that the same adventurer cannot be added twice."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    assert adventurer in party.members
    
    with pytest.raises(ValueError, match="Adventurer is already in the party"):
        party.add_member(adventurer)
    
    assert len(party.members) == 1


def test_add_member_not_available() -> None:
    """Tests that an injured or retired adventurer cannot join the party."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    adventurer.injured()
    assert adventurer.status == AdventurerStatus.INJURED

    with pytest.raises(ValueError, match="Adventurer is not available to join the party"):
        party.add_member(adventurer)
    assert len(party.members) == 0
    
    adventurer.recover()
    assert adventurer.status == AdventurerStatus.AVAILABLE
    
    adventurer.retire()
    assert adventurer.status == AdventurerStatus.RETIRED
    
    with pytest.raises(ValueError, match="Adventurer is not available to join the party"):
        party.add_member(adventurer)
    assert len(party.members) == 0


def test_add_member_to_full_party() -> None:
    """Tests to add an adventurer to a full party."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer2 = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)
    adventurer3 = Adventurer("adv-003", "Fox", AdventurerClass.WARRIOR, 1)
    adventurer4 = Adventurer("adv-004", "Sox", AdventurerClass.WARRIOR, 1)
    adventurer5 = Adventurer("adv-005", "Pox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.add_member(adventurer2)
    party.add_member(adventurer3)
    party.add_member(adventurer4)
    assert len(party.members) == party.max_members

    with pytest.raises(ValueError, match=f"Cannot have more than {party.max_members} adventurers in a party"):
        party.add_member(adventurer5)
    assert len(party.members) == party.max_members
    assert adventurer5.status == AdventurerStatus.AVAILABLE


### ---------- Remove from Party Tests ---------- ###
def test_remove_member() -> None:
    """Tests removing an adventurer from the party."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    assert adventurer in party.members
    assert adventurer.status == AdventurerStatus.ASSIGNED
    
    party.remove_member(adventurer)
    assert adventurer not in party.members
    assert adventurer.status == AdventurerStatus.AVAILABLE


def test_remove_member_not_in_party() -> None:
    """Tests to remove a member that is not in the party."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    assert len(party.members) == 0
    
    with pytest.raises(ValueError, match="Adventurer is not in the party"):
        party.remove_member(adventurer)
    assert len(party.members) == 0
    assert adventurer.status == AdventurerStatus.AVAILABLE