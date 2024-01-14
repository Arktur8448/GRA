class NPC:                                                                                     # tablica
    def __init__(self, level, exp_drop, health, mana, strength, defence, agility, race, weapon, drop, dialogues):
        self.level = level
        self.exp_drop = exp_drop
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.agility = agility
        self.race = race
        self.weapon = weapon
        self.drop = drop
        self.dialogues = dialogues

    def interact(self, option):
        if option is None:
            return self.dialogues[0]
        else:
            return self.dialogues[option]

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

# dialogues = piszesz w tablicy !!!1!!!!!111!!
# drop = piszesz w tablicy też !!!1!!!!!111!!