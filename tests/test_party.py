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
    assert party.leader is None
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


### ---------- Party Size Tests ---------- ###
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


def test_new_party_is_not_full() -> None:
    """Tests that new party is not already full."""
    party = Party("12345", "Nox's Party")
    assert not party.is_full()


def test_party_is_full_at_max_members() -> None:
    """Tests that party is full at max members."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer2 = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)
    adventurer3 = Adventurer("adv-003", "Fox", AdventurerClass.WARRIOR, 1)
    adventurer4 = Adventurer("adv-004", "Sox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.add_member(adventurer2)
    party.add_member(adventurer3)
    party.add_member(adventurer4)
    assert party.is_full()


def test_party_member_count_zero() -> None:
    """Tests party member count is zero."""
    party = Party("12345", "Nox's Party")
    assert party.member_count == 0


def test_party_member_count_one() -> None:
    """Tests party member count with one adventurer."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    assert party.member_count == 1


### ---------- Party Name Tests ---------- ###
def test_party_name_whitespace_only() -> None:
    """Tests that the party name contains only whitespaces."""
    with pytest.raises(ValueError, match="Party name cannot be empty"):
        Party("12345", "   ")


def test_party_name_length_short() -> None:
    """Tests that a party name shorter than 3 characters is rejected."""
    with pytest.raises(ValueError, match="Party name must be between 3 and 30 characters"):
        Party("12345", "No")


def test_party_name_length_long() -> None:
    """Tests that a party name longer than 30 characters is rejected."""
    with pytest.raises(ValueError, match="Party name must be between 3 and 30 characters"):
        Party("12345", "Nox's Party Name Is Far Too Long")


def test_party_name_whitespace_before_after() -> None:
    """Tests that a party name with leading and trailing whitespaces are removed."""
    party = Party("12345", "     Nox's Party     ")
    assert party.name == "Nox's Party"


### ---------- Party Name Tests ---------- ###
def test_assign_party_leader() -> None:
    """Tests that the party has no leader then updates the leader to the adventurer."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    assert party.leader is None
    
    party.add_member(adventurer)
    party.assign_leader(adventurer)
    assert party.leader is adventurer


def test_assign_party_leader_not_in_party() -> None:
    """Tests that the party has no leader then fails to update adventurer not in party as leader."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    assert party.leader is None
    
    with pytest.raises(ValueError, match="Leader must be in the party"):
        party.assign_leader(adventurer)


def test_assign_new_leader_from_existing() -> None:
    """Tests that the party has a leader, then fails to update the leader to another party member."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    adventurer2 = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.assign_leader(adventurer)
    assert party.leader is adventurer
    
    party.add_member(adventurer2)
    with pytest.raises(ValueError, match=f"Nox is already the party leader"):
        party.assign_leader(adventurer2)
    assert party.leader is adventurer


def test_removing_member_from_party() -> None:
    """Tests that the adventurer is removed from the party and their status is updated to available."""
    adventurer = Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.assign_leader(adventurer)
    assert party.leader is adventurer
    
    party.remove_member(adventurer)
    assert party.leader is None
    assert adventurer not in party.members
    assert adventurer.status == AdventurerStatus.AVAILABLE


# TO DO: Create tests for available slots!