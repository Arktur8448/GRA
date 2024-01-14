class Item:
    def __init__(self, typee, name, consumable, price_buy, price_sell):
        self.typee = typee
        self.name = name
        self.consumable = consumable
        self.price_buy = price_buy
        self.price_sell = price_sell


class Weapon(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.strength_requirement = strength_requirement
        self.agility_requirement = agility_requirement
        self.damage = damage
        self.speed = speed

    def check_weapon(self, player_strength, player_agility):
        if self.strength_requirement < player_strength and self.agility_requirement < player_agility:
            return True
        else:
            return False


class Armor(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, defence):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.strength_requirement = strength_requirement
        self.defence = defence

    def check_weapon(self, player_defence):
        if self.strength_requirement < player_defence:
            return True
        else:
            return False


class Sword(Weapon):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed, slash_damage, slash_damage_mana_requirement):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed)
        self.slash_damage = slash_damage
        self.slash_damage_mana_requirement = slash_damage_mana_requirement


class Axe(Weapon):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed, chop_damage, chop_damage_mana_requirement):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed)
        self.chop_damage = chop_damage
        self.chop_damage_mana_requirement = chop_damage_mana_requirement

# speed = co ile sekund atak od momentu kliknienioa przycisku
# template : Sword_blahblah = Sword("sword", "Sword_blahblah", False, 500, 400, 25, 10, 30, 2, 50, 25)
# items = [None, Sword_blahblah, axe_coścoś, itp...]
