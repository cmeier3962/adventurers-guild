from eryndor.enums import QuestDifficulty, QuestStatus
from eryndor.party import Party


class Quest:
    """Creates a Quest object for storing quest information"""
    
    def __init__(
        self,
        quest_id: str,
        name: str,
        description: str,
        difficulty: QuestDifficulty,
        reward_gold: int,
    ) -> None:
        self.quest_id = quest_id
        
        quest_name = name.strip()
        if quest_name == "":
            raise ValueError("Quest name cannot be empty.")
        if len(quest_name) < 3 or len(quest_name) > 50:
            raise ValueError("Quest name must be between 3 and 50 characters.")
        self.name = quest_name
        
        quest_description = description.strip()
        if quest_description == "":
            raise ValueError("Quest description cannot be empty.")
        if len(quest_description) < 10:
            raise ValueError("Quest description must be at least 10 characters.")
        self.description = quest_description
        
        self.difficulty = difficulty
        
        if reward_gold < 0:
            raise ValueError("Gold reward must be zero or higher.")
        self.reward_gold = reward_gold
        
        self.status = QuestStatus.NOT_STARTED
        
        self.assigned_party: Party | None = None
    
    
    def start(self) -> None:
        """Checks if the quest status is 'Not Started' and then update it to 'In progress'."""
        if self.assigned_party is None:
            raise ValueError("You must have a party to start this quest.")
        if self.status is not QuestStatus.NOT_STARTED:
            raise ValueError("Only quests that have not started can be started.")
        
        self.status = QuestStatus.IN_PROGRESS
    
    
    def complete(self) -> None:
        """Check that the quest is not already completed, is in progress, and updates it to complete."""
        if self.status is not QuestStatus.IN_PROGRESS:
            raise ValueError("Quests can only be completed if they are currently in progress.")
        
        self.status = QuestStatus.COMPLETED


    def abandon(self) -> None:
        """Check that the quest is in progress and then updates it to not started."""
        if self.status is not QuestStatus.IN_PROGRESS:
            raise ValueError("Only quests in progress can be abandoned.")
        
        self.status = QuestStatus.NOT_STARTED
    
    
    def assign_party(self, party: Party) -> None:
        """Checks the following:
            - Quest is not started
            - Party has at least one member
            - Party has a leader
            - Quest does not already have a party assigned
        """
        if self.status is not QuestStatus.NOT_STARTED:
            raise ValueError("Parties can only be assigned to quests that have not started.")
        if party.member_count == 0:
            raise ValueError("Party must have at least one member.")
        if party.leader is None:
            raise ValueError("Party must have a leader.")
        if self.assigned_party is not None:
            raise ValueError("Quest already has an assigned party.")
        
        self.assigned_party = party