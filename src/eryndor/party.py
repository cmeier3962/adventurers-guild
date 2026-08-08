from eryndor.adventurer import Adventurer
from eryndor.enums import AdventurerStatus


class Party:
    """Represents a party of adventurers."""

    def __init__(
        self,
        party_id: str,
        name: str,
    ) -> None:
        self.party_id = party_id
        
        party_name = name.strip()
        if party_name == "":
            raise ValueError("Party name cannot be empty.")
        if len(party_name) < 3 or len(party_name) > 30:
            raise ValueError("Party name must be between 3 and 30 characters.")
        self.name = party_name
        
        self.leader: Adventurer | None = None
        self.members: list[Adventurer] = []
        self.max_members: int = 4


    @property
    def member_count(self) -> int:
        """Returns the count of party members."""
        return len(self.members)


    @property
    def available_slots(self) -> int:
        """Return the number of open member slots."""
        return self.max_members - self.member_count


    def is_full(self) -> bool:
        """Checks if party is full."""
        return self.member_count >= self.max_members


    def add_member(self, adventurer: Adventurer) -> None:
        """Adds a member to the party and updates their status to assigned."""
        if adventurer in self.members:
            raise ValueError("Adventurer is already in the party.")

        if adventurer.status != AdventurerStatus.AVAILABLE:
            raise ValueError("Adventurer is not available to join the party.")
        
        if self.is_full():
            raise ValueError(f"Cannot have more than {self.max_members} adventurers in a party!")
        
        self.members.append(adventurer)
        adventurer.status = AdventurerStatus.ASSIGNED


    def remove_member(self, adventurer: Adventurer) -> None:
        """Removes a member from the party and updates their status to available."""
        if adventurer not in self.members:
            raise ValueError("Adventurer is not in the party.")
        
        if self.leader is adventurer:
            self.leader = None

        self.members.remove(adventurer)
        adventurer.status = AdventurerStatus.AVAILABLE


    def assign_leader(self, adventurer: Adventurer) -> None:
        """Checks if adventurer exists in the party, then assigns them as leader."""
        if adventurer not in self.members:
            raise ValueError("Leader must be in the party.")
        
        if self.leader is not None:
            raise ValueError(f"{self.leader.username} is already the party leader.")
        
        self.leader = adventurer


    def change_leader(self, adventurer: Adventurer) -> None:
        """Verifies the party already has a leader, then checks if the adventurer is in the party, 
        and then updates the leader to that adventurer."""
        if self.leader is None:
            raise ValueError("Party has no leader.")
        
        if adventurer not in self.members:
            raise ValueError("Adventurer is not in the party.")
        
        if self.leader is adventurer:
            raise ValueError("Adventurer is already the party leader.")
        
        self.leader = adventurer