import arcade
import items
import inventory


class NPC (arcade.Sprite):
    def __init__(self, filename, name, description, level, exp_drop, health, strength, defence, agility, race,
                 weapon=None, drop=None, to_sell=None):
        super().__init__(filename=filename)
        self.name = name
        self.description = description
        self.level = level
        self.exp_drop = exp_drop
        self.health = health
        self.max_health = self.health
        self.strength = strength
        self.defence = defence
        self.agility = agility
        self.race = race
        self.weapon = weapon if weapon else []
        self.drop = drop if drop else []
        self.to_sell = to_sell if to_sell else []
        # jako tablica 2 wymiarowa [[(tutaj dajesz item który zrobisz używając klasy), cena], itd...] np.: (Health_Potion, Health_Potion.price_buy

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

# class Mage(NPC):
#     pass
#     def use_spell(self, player):
#         pass
