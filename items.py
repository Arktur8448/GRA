class Item:
    def __init__(self, typee, name, consumable, stackable):
        self.typee = typee
        self.name = name
        self.consumable = consumable
        self.stackable = stackable


items = [
    Item("heal", "Small Potion Health", True, True),
    Item("heal", "Big Potion Health", True, True),
    Item("heal", "Small Potion Mana", True, True),
    Item("heal", "Big Potion Mana", True, True),
    Item("heal", "Small Rejuvenation Potion", True, True),
    Item("heal", "Big Rejuvenation Potion", True, True),
    Item("heal", "Stamina Potion", True, True),
    Item("heal", "Antidote Potion ", True, True),
    Item("heal", "Gas Potion", True, True),
    Item("heal", "Oil Potion", True, True),
    Item("heal", "Thawing Potion", True, True),
    Item("key", "Key", False, True),
    Item("amulet", "Silver Amulet", False, False),
    Item("amulet", "Gold Amulet", False, False),
    Item("amulet", "Diamond Amulet", False, False),
    Item("ring", "Wooden Ring", False, False),
    Item("ring", "Ring of The Witcher", False, False),
    Item("ring", "Zombie's Ring", False, False),
    Item("ring", "Villager's Ring", False, False),
    Item("ring", "Ring of The King", False, False),
    Item("charm", "Charm of The Attack", False, False),
    Item("charm", "Charm of The Iron", False, False),
    Item("charm", "Charm of The Strength", False, False),
    Item("charm", "Charm of The Steel", False, False),
    Item("charm", "Charm of The Fire", False, False),
    Item("gem", "Silver", False, True),
    Item("gem", "Iron", False, True),
    Item("gem", "Gold", False, True),
    Item("gem", "Diamond", False, True),
    Item("gem", "Emerald", False, True),
    Item("ore", "Log", False, True),
    Item("ore", "Stick", False, True),
    Item("ore", "Rock", False, True),
    Item("ore", "Rope", False, True),
    Item("sword", "Sword of The King", False, False),
    Item("sword", "Sword of The Witcher", False, False),
    Item("sword", "Sword of The Grandfather", False, False),
    Item("sword", "Sword of The Zombie", False, False),
    Item("sword", "Sword of The ", False, False),

]
