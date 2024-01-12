import  arcade
class Player:
    def __init__(self, x=0, y=0 , sprite=None):
        self.playerSprite = sprite
        self.movment_speed = 10
        self.x = x
        self.y = y

        self.level = 1  # base staty
        self.exp = 0
        self.attribute_points = 0
        self.health = 25
        self.mana = 10
        self.strength = 10
        self.defence = 10
        self.agility = 10
        self.race = None
        self.weapon = None

    def update_sprite(self):
        self.playerSprite.center_x = self.x
        self.playerSprite.center_y = self.y

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
