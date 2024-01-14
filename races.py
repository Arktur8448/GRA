class Race:
    def __init__(self, name, health, mana,strength, defence, agility):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.agility = agility


Human = Race("Human", 25, 5, 10, 5, 5)

# races = [Human, Elf, itp...]
