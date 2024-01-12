from items import Item


class Armor(Item):
    def __init__(self, typee, name, consumable, stackable, strength_requirement, defence):
        super().__init__(typee, name, consumable, stackable)
        self.strength_requirement = strength_requirement
        self.defence = defence

    def check_weapon(self, player_defence):
        if self.strength_requirement < player_defence:
            return True
        else:
            return False