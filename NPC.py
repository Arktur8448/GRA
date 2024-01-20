class NPC:                                                                                     # tablica
    def __init__(self, name, description, level, exp_drop, health, mana, strength, defence, agility, race, weapon, drop, to_sell, dialogues):
        self.name = name
        self.description = description # opis npc'ta
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
        self.to_sell = to_sell
        # jako tablica 2 wymiarowa [[(tutaj dajesz item który zrobisz używając klasy), cena], itd...] np.: (Health_Potion, Health_Potion.price_buy)
        self.dialogues = dialogues

    def interact(self, option):
        if option is None:
            return self.dialogues[0]
        else:
            return self.dialogues[option]

    # def buy(self, option, players_money):
    #     if players_money >= self.to_sell[option][1]:
    #         Player.inventory.append(self.to_sell[option][0]) nwm coś w tym stylu jak będzie inventory to zronbie
    #         return players_money-self.to_sell[option][1]
    #     else:
    #         return False
    # coś w tym stylu nwm

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

# dialogues = piszesz w tablicy !!!1!!!!!111!!
# drop = piszesz w tablicy też !!!1!!!!!111!!
# a to_sell? też w TABLICY !!!1!!!11!!!!1