import pytest

from eryndor.adventurer import Adventurer
from eryndor.enums import AdventurerClass, AdventurerStatus
from eryndor.party import Party


### ---------- Fixtures ---------- ###
@pytest.fixture
def adventurer() -> Adventurer:
    """Returns a valid adventurer."""
    return Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)


@pytest.fixture
def empty_party() -> Party:
    """Returns an empty party with no members or leader."""
    return Party("12345", "Nox's Party")


@pytest.fixture
def party(adventurer: Adventurer) -> Party:
    """Returns a valid party with one member and a leader."""
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.assign_leader(adventurer)
    return party


@pytest.fixture
def party_with_member_no_leader(adventurer: Adventurer) -> Party:
    """Returns a party with a member but no leader."""
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    return party


### ---------- Initialize Class Tests ---------- ###
def test_empty_party(empty_party: Party) -> None:
    """Tests a predefined party."""
    assert empty_party.id == "12345"
    assert empty_party.name == "Nox's Party"
    assert empty_party.leader is None
    assert empty_party.members == []


### ---------- Party Name Tests ---------- ###
def test_party_name_whitespace_only() -> None:
    """Tests that the party name contains only whitespaces."""
    with pytest.raises(ValueError, match="Party name cannot be empty"):
        Party("12345", "   ")


def test_party_name_length_short() -> None:
    """Tests that a party name shorter than 3 characters is rejected."""
    with pytest.raises(
        ValueError,
        match="Party name must be between 3 and 30 characters",
    ):
        Party("12345", "No")


def test_party_name_length_long() -> None:
    """Tests that a party name longer than 30 characters is rejected."""
    with pytest.raises(
        ValueError,
        match="Party name must be between 3 and 30 characters",
    ):
        Party("12345", "Nox's Party Name Is Far Too Long")


def test_party_name_whitespace_before_after() -> None:
    """Tests that a party name with leading and trailing whitespaces are removed."""
    party = Party("12345", "     Nox's Party     ")
    assert party.name == "Nox's Party"


### ---------- Add to Party Tests ---------- ###
def test_add_member(adventurer: Adventurer, empty_party: Party) -> None:
    """Tests adding an adventurer to the party."""
    empty_party.add_member(adventurer)

    assert adventurer in empty_party.members
    assert adventurer.status is AdventurerStatus.ASSIGNED


def test_add_member_duplicate(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests that the same adventurer cannot be added twice."""
    empty_party.add_member(adventurer)

    with pytest.raises(
        ValueError,
        match="Adventurer is already in the party",
    ):
        empty_party.add_member(adventurer)

    assert len(empty_party.members) == 1


def test_add_member_not_available(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests that an injured or retired adventurer cannot join the party."""
    adventurer.injured()

    with pytest.raises(
        ValueError,
        match="Adventurer is not available to join the party",
    ):
        empty_party.add_member(adventurer)

    assert len(empty_party.members) == 0

    adventurer.recover()
    adventurer.retire()

    with pytest.raises(
        ValueError,
        match="Adventurer is not available to join the party",
    ):
        empty_party.add_member(adventurer)

    assert len(empty_party.members) == 0


### ---------- Remove from Party Tests ---------- ###
def test_remove_member(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests removing an adventurer from the party."""
    empty_party.add_member(adventurer)

    empty_party.remove_member(adventurer)

    assert adventurer not in empty_party.members
    assert adventurer.status is AdventurerStatus.AVAILABLE


def test_remove_member_not_in_party(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests removing a member that is not in the party."""
    with pytest.raises(
        ValueError,
        match="Adventurer is not in the party",
    ):
        empty_party.remove_member(adventurer)

    assert len(empty_party.members) == 0
    assert adventurer.status is AdventurerStatus.AVAILABLE


### ---------- Party Size Tests ---------- ###
def test_add_member_to_full_party() -> None:
    """Tests adding an adventurer to a full party."""
    adventurers = [
        Adventurer(f"adv-00{i}", name, AdventurerClass.WARRIOR, 1)
        for i, name in enumerate(["Nox", "Box", "Fox", "Sox", "Pox"], start=1)
    ]

    party = Party("12345", "Nox's Party")

    for adventurer in adventurers[:4]:
        party.add_member(adventurer)

    assert len(party.members) == party.max_members

    with pytest.raises(
        ValueError,
        match=f"Cannot have more than {party.max_members} adventurers in a party",
    ):
        party.add_member(adventurers[4])

    assert len(party.members) == party.max_members
    assert adventurers[4].status is AdventurerStatus.AVAILABLE


def test_new_party_is_not_full(empty_party: Party) -> None:
    """Tests that a new party is not already full."""
    assert not empty_party.is_full()


def test_party_is_full_at_max_members() -> None:
    """Tests that party is full at max members."""
    adventurers = [
        Adventurer(f"adv-00{i}", name, AdventurerClass.WARRIOR, 1)
        for i, name in enumerate(["Nox", "Box", "Fox", "Sox"], start=1)
    ]

    party = Party("12345", "Nox's Party")

    for adventurer in adventurers:
        party.add_member(adventurer)

    assert party.is_full()


def test_party_member_count_zero(empty_party: Party) -> None:
    """Tests party member count is zero."""
    assert empty_party.member_count == 0


def test_party_member_count_one(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests party member count with one adventurer."""
    empty_party.add_member(adventurer)

    assert empty_party.member_count == 1


def test_available_slots_new_party(empty_party: Party) -> None:
    """Tests that a new party has all slots available."""
    assert empty_party.available_slots == 4


def test_available_slots(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests available slots are accurate."""
    empty_party.add_member(adventurer)

    assert empty_party.available_slots == 3


### ---------- Party Leader Assignment Tests ---------- ###
def test_assign_party_leader(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests assigning an adventurer as party leader."""
    empty_party.add_member(adventurer)

    empty_party.assign_leader(adventurer)

    assert empty_party.leader is adventurer


def test_assign_party_leader_not_in_party(
    adventurer: Adventurer,
    empty_party: Party,
) -> None:
    """Tests assigning an adventurer not in the party as leader fails."""
    with pytest.raises(
        ValueError,
        match="Leader must be in the party",
    ):
        empty_party.assign_leader(adventurer)


def test_assign_new_leader_from_existing(
    party: Party,
) -> None:
    """Tests that a party cannot assign a second leader."""
    adventurer = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)
    
    party.add_member(adventurer)

    with pytest.raises(
        ValueError,
        match="Nox is already the party leader",
    ):
        party.assign_leader(adventurer)

    assert party.leader is not None
    assert party.leader.username == "Nox"


### ---------- Party Leader Change Tests ---------- ###
def test_removing_leader_from_party(
    party: Party,
    adventurer: Adventurer,
) -> None:
    """Tests removing the party leader removes them from the party."""
    party.remove_member(adventurer)

    assert party.leader is None
    assert adventurer not in party.members
    assert adventurer.status is AdventurerStatus.AVAILABLE


def test_change_leader_not_in_party(
    party: Party,
) -> None:
    """Tests changing leader fails if adventurer is not in the party."""
    adventurer = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)

    with pytest.raises(
        ValueError,
        match="Adventurer is not in the party",
    ):
        party.change_leader(adventurer)

    assert party.leader is not None
    assert party.leader.username == "Nox"


def test_change_leader_no_leader(
    party_with_member_no_leader: Party,
    adventurer: Adventurer,
) -> None:
    """Tests changing leader fails if no leader exists."""
    with pytest.raises(
        ValueError,
        match="Party has no leader",
    ):
        party_with_member_no_leader.change_leader(adventurer)

    assert party_with_member_no_leader.leader is None


def test_change_leader_already_leader(
    party: Party,
    adventurer: Adventurer,
) -> None:
    """Tests changing leader fails when adventurer is already leader."""
    with pytest.raises(
        ValueError,
        match="Adventurer is already the party leader",
    ):
        party.change_leader(adventurer)

    assert party.leader is adventurer


def test_change_leader(party: Party) -> None:
    """Tests changing leader updates to another party member."""
    adventurer = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)

    party.add_member(adventurer)
    party.change_leader(adventurer)

    assert party.leader is adventurer