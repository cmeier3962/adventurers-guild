import pytest

from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, QuestDifficulty, QuestStatus
from adventurers_guild.party import Party
from adventurers_guild.quest import Quest


### ---------- Fixtures ---------- ###
@pytest.fixture
def adventurer() -> Adventurer:
    """Returns a valid adventurer."""
    return Adventurer("adv-001", "Nox", AdventurerClass.WARRIOR, 1)


@pytest.fixture
def party(adventurer: Adventurer) -> Party:
    """Returns a valid party with one member and a leader."""
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)
    party.assign_leader(adventurer)
    return party


@pytest.fixture
def quest() -> Quest:
    """Returns a valid quest."""
    return Quest(
        "quest-001",
        "New Beginnings",
        "This quest will be the start of the tutorial.",
        QuestDifficulty.EASY,
        100,
    )


@pytest.fixture
def assigned_quest(party: Party, quest: Quest) -> Quest:
    """Returns a valid quest with an assigned party."""
    quest.assign_party(party)
    return quest


@pytest.fixture
def in_progress_quest(assigned_quest: Quest) -> Quest:
    """Returns a valid quest that is currently in progress."""
    assigned_quest.start()
    return assigned_quest


### ---------- Initialize Class Tests ---------- ###
def test_quest(quest: Quest) -> None:
    """Tests the creation of a Quest object."""
    assert quest.quest_id == "quest-001"
    assert quest.name == "New Beginnings"
    assert quest.description == "This quest will be the start of the tutorial."
    assert quest.difficulty is QuestDifficulty.EASY
    assert quest.reward_gold == 100
    assert quest.status is QuestStatus.NOT_STARTED


def test_quest_zero_gold(quest: Quest) -> None:
    """Tests the creation of a Quest object with zero gold reward."""
    quest.reward_gold = 0

    assert quest.reward_gold == 0


def test_quest_negative_gold() -> None:
    """Tests creating a quest with negative gold fails."""
    with pytest.raises(ValueError, match="Gold reward must be zero or higher"):
        Quest(
            "quest-001",
            "New Beginnings",
            "This quest will be the start of the tutorial.",
            QuestDifficulty.EASY,
            -100,
        )


### ---------- Quest Name Tests ---------- ###
def test_quest_name_whitespace_only() -> None:
    """Tests that the quest name cannot contain only whitespaces."""
    with pytest.raises(ValueError, match="Quest name cannot be empty"):
        Quest(
            "quest-001",
            "   ",
            "This quest will be the start of the tutorial.",
            QuestDifficulty.EASY,
            100,
        )


def test_quest_name_whitespace_before_after(quest: Quest) -> None:
    """Tests that leading and trailing quest name whitespaces are removed."""
    quest = Quest(
        "quest-001",
        "   New Beginnings   ",
        quest.description,
        QuestDifficulty.EASY,
        100,
    )

    assert quest.name == "New Beginnings"


def test_quest_name_length_short() -> None:
    """Tests that a quest name shorter than 3 characters is rejected."""
    with pytest.raises(ValueError, match="Quest name must be between 3 and 50 characters"):
        Quest(
            "quest-001",
            "Ne",
            "This quest will be the start of the tutorial.",
            QuestDifficulty.EASY,
            100,
        )


def test_quest_name_length_long() -> None:
    """Tests that a quest name longer than 50 characters is rejected."""
    with pytest.raises(ValueError, match="Quest name must be between 3 and 50 characters"):
        Quest(
            "quest-001",
            "A" * 51,
            "This quest will be the start of the tutorial.",
            QuestDifficulty.EASY,
            100,
        )


### ---------- Quest Description Tests ---------- ###
def test_quest_description_whitespace_only() -> None:
    """Tests that the quest description cannot contain only whitespaces."""
    with pytest.raises(ValueError, match="Quest description cannot be empty"):
        Quest(
            "quest-001",
            "New Beginnings",
            "     ",
            QuestDifficulty.EASY,
            100,
        )


def test_quest_description_whitespace_before_after() -> None:
    """Tests that leading and trailing description whitespaces are removed."""
    quest = Quest(
        "quest-001",
        "New Beginnings",
        "     This quest will be the start of the tutorial.     ",
        QuestDifficulty.EASY,
        100,
    )

    assert quest.description == "This quest will be the start of the tutorial."


def test_quest_description_length_short() -> None:
    """Tests that a quest description shorter than 10 characters is rejected."""
    with pytest.raises(ValueError, match="Quest description must be at least 10 characters"):
        Quest(
            "quest-001",
            "New Beginnings",
            "Quest",
            QuestDifficulty.EASY,
            100,
        )


### ---------- Quest Status Tests ---------- ###
def test_start_quest(assigned_quest: Quest) -> None:
    """Tests starting a quest updates status to in progress."""
    assert assigned_quest.status is QuestStatus.NOT_STARTED

    assigned_quest.start()

    assert assigned_quest.status is QuestStatus.IN_PROGRESS


def test_start_quest_without_party(quest: Quest) -> None:
    """Tests that a quest cannot start without an assigned party."""
    assert quest.assigned_party is None
    assert quest.status is QuestStatus.NOT_STARTED

    with pytest.raises(ValueError, match="You must have a party to start this quest"):
        quest.start()

    assert quest.status is QuestStatus.NOT_STARTED


def test_quest_status_already_started(in_progress_quest: Quest) -> None:
    """Tests that an already started quest cannot be started again."""
    with pytest.raises(ValueError, match="Only quests that have not started can be started"):
        in_progress_quest.start()


def test_quest_status_complete(in_progress_quest: Quest) -> None:
    """Tests updating a quest status to completed."""
    in_progress_quest.complete()

    assert in_progress_quest.status is QuestStatus.COMPLETED


def test_complete_quest_not_in_progress(quest: Quest) -> None:
    """Tests that a quest cannot be completed before starting."""
    with pytest.raises(
        ValueError,
        match="Quests can only be completed if they are currently in progress",
    ):
        quest.complete()

    assert quest.status is QuestStatus.NOT_STARTED


def test_abandon_quest(in_progress_quest: Quest) -> None:
    """Tests updating a quest status back to not started when abandoned."""
    in_progress_quest.abandon()

    assert in_progress_quest.status is QuestStatus.NOT_STARTED


def test_abandon_quest_not_in_progress(quest: Quest) -> None:
    """Tests that a quest cannot be abandoned before starting."""
    with pytest.raises(
        ValueError,
        match="Only quests in progress can be abandoned",
    ):
        quest.abandon()

    assert quest.status is QuestStatus.NOT_STARTED


### ---------- Assign Party Tests ---------- ###
def test_assign_party(quest: Quest, party: Party) -> None:
    """Tests assigning a party to a quest."""
    assert quest.assigned_party is None

    quest.assign_party(party)

    assert quest.assigned_party is party


def test_party_already_assigned_quest(
    assigned_quest: Quest,
    party: Party,
) -> None:
    """Tests that a quest cannot be assigned another party."""
    party2 = Party("67890", "Box's Party")
    adventurer2 = Adventurer("adv-002", "Box", AdventurerClass.WARRIOR, 1)

    party2.add_member(adventurer2)
    party2.assign_leader(adventurer2)

    with pytest.raises(
        ValueError,
        match="Quest already has an assigned party",
    ):
        assigned_quest.assign_party(party2)

    assert assigned_quest.assigned_party is party


def test_assign_party_to_quest_in_progress(in_progress_quest: Quest, party: Party) -> None:
    """Tests that a party cannot be assigned after quest starts."""
    with pytest.raises(
        ValueError,
        match="Parties can only be assigned to quests that have not started",
    ):
        in_progress_quest.assign_party(party)

    assert in_progress_quest.assigned_party is party


def test_assign_party_to_quest_with_no_members(quest: Quest) -> None:
    """Tests assigning an empty party fails."""
    party = Party("12345", "Nox's Party")

    with pytest.raises(
        ValueError,
        match="Party must have at least one member",
    ):
        quest.assign_party(party)

    assert quest.assigned_party is None


def test_assign_party_to_quest_with_no_leader(
    quest: Quest,
    adventurer: Adventurer,
) -> None:
    """Tests assigning a party without a leader fails."""
    party = Party("12345", "Nox's Party")
    party.add_member(adventurer)

    with pytest.raises(
        ValueError,
        match="Party must have a leader",
    ):
        quest.assign_party(party)

    assert quest.assigned_party is None