from eryndor.enums import ItemType, ItemRarity


class Item:
    """Creates an item object."""
    
    def __init__(
        self,
        item_id: str,
        name: str,
        description: str,
        item_type: ItemType,
        rarity: ItemRarity,
        value: int
    ) -> None:
        self.id = item_id
        
        item_name = name.strip()
        if item_name == "":
            raise ValueError("Item name cannot be blank.")
        if len(item_name) < 3 or len(item_name) > 50:
            raise ValueError("Item name must be between 3 and 50 characters.")
        self.name = item_name
        
        item_description = description.strip()
        if item_description == "":
            raise ValueError("Item description cannot be blank.")
        if len(item_description) < 5:
            raise ValueError("Item description must be at least 5 characters.")
        self.description = item_description
        
        self.item_type = item_type
        
        self.rarity = rarity
        
        if value < 0:
            raise ValueError("Item value cannot be less than 0.")
        self.value = value