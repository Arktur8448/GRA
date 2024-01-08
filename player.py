import  items # import pliku items.py
class Player:
    def __init__(self, x=0, y=0):
        self.playerSprite = None
        self.x = x
        self.y = y
        self.velocity_x, self.velocity_y = 100.0, 100.0
        self.level = 1  # base staty
        self.exp = 0
        self.attribute_points = 0
        self.health = 25
        self.mana = 10
        self.strength = 10
        self.defence = 10
        self.agility = 10
        # world_race[1][2] to zwiększenie do podstawowego hp world_race[1][3] to zwiększenie do podstawowej Many itd...
        self.world_races = [None,
                            [1, "Human", 25, 10, 10, 15, 5],
                            [2, "Elf", 15, 25, 5, 5, 25],
                            [3, "Dwarf", 35, 5, 25, 20, 5]
                            ]
        self.race = None
        # weapon[][2 i 3] to minnimalne wymagania (siła, zwinność)
        self.arsenal = [None,
                        [1, "Fist", 0, 0],
                        [2, "Log", 25, 5],
                        [3, "Dagger", 10, 20],
                        [4, "Sledge Hammer", 40, 10]
                        ]
        self.weapon = self.arsenal[1]
        # self.condition = None (np poison, bleeding ale to jest WIP)

    def update_sprite(self):
        self.playerSprite.x = self.x
        self.playerSprite.y = self.y

    def set_weapon(self, weapon_id):
        if self.strength >= self.arsenal[weapon_id][2] and self.agility >= self.arsenal[weapon_id][3]:
            self.weapon = self.arsenal[weapon_id]
            return True
        else:
            return False

    def set_race(self, given_race_id):
        # staty podstawowe zwiększone o staty rasy (możliwość hardmodu bez rasy!?!??!)
        if self.race is None:
            self.race = given_race_id
            self.health += self.world_races[given_race_id][2]
            self.mana += self.world_races[given_race_id][3]
            self.strength += self.world_races[given_race_id][4]
            self.defence += self.world_races[given_race_id][5]
            self.agility += self.world_races[given_race_id][6]
            return True
        else:
            return False

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def level_up(self):
        if self.exp >= self.level*50:
            self.level += 1
            self.attribute_points += 1
            return True
        else:
            return self.level*50-self.exp

    def redistribute_points(self, stat):
        if stat == "1":
            self.health += 10
            return True
        elif stat == "2":
            self.mana += 10
            return True
        elif stat == "3":
            self.strength += 5
            return True
        elif stat == "4":
            self.defence += 5
            return True
        elif stat == "5":
            self.agility += 5
            return True
        else:
            return False
