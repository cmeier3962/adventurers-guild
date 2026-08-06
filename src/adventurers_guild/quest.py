from adventurers_guild.adventurer import Adventurer
from adventurers_guild.enums import AdventurerClass, AdventurerStatus, QuestDifficulty, QuestStatus


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