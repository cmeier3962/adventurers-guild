from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, AdventurerStatus


class Party:
    """Represents a party of adventurers."""
    def __init__(
        self,
        party_id: str,
        name: str,
    ) -> None:
        self.party_id = party_id
        self.name = name
        self.members: list[Adventurer] = []
        self.max_members: int = 4


    def add_member(self, adventurer: Adventurer) -> None:
        """Adds a member to the party and updates their status to assigned."""
        if adventurer in self.members:
            raise ValueError("Adventurer is already in the party.")

        if adventurer.status != AdventurerStatus.AVAILABLE:
            raise ValueError("Adventurer is not available to join the party.")
        
        if len(self.members) >= self.max_members:
            raise ValueError(f"Cannot have more than {self.max_members} adventurers in a party!")
        
        self.members.append(adventurer)
        adventurer.status = AdventurerStatus.ASSIGNED


    def remove_member(self, adventurer: Adventurer) -> None:
        """Removes a member from the party and updates their status to available."""
        if adventurer not in self.members:
            raise ValueError("Adventurer is not in the party.")
        
        self.members.remove(adventurer)
        adventurer.status = AdventurerStatus.AVAILABLE