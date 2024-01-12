from items import Item


class Weapon(Item):
    def __init__(self, typee, name, consumable, stackable, strength_requirement, agility_requirement, damage, speed):
        super().__init__(typee, name, consumable, stackable)
        self.strength_requirement = strength_requirement
        self.agility_requirement = agility_requirement
        self.damage = damage
        self.speed = speed

    def check_weapon(self, player_strength, player_agility):
        if self.strength_requirement < player_strength and self.agility_requirement < player_agility:
            return True
        else:
            return False
