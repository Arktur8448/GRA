class Item:
    def __init__(self, typee, name, consumable, price_buy, price_sell):
        self.typee = typee
        self.name = name
        self.consumable = consumable
        self.price_buy = price_buy
        self.price_sell = price_sell


class Food(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell,adds_food):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.adds_food = adds_food


class Weapon_Upgrader(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell,type_weapon,special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.type_weapon = type_weapon
        self.special_effect = special_effect


class Armor_Upgrader(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell,type_armor,special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.type_weapon = type_armor
        self.special_effect = special_effect


class Ore(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell,mining_lucky):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.mining_lucky = mining_lucky


class Key(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell, special_effect, key_lvl):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.special_effect = special_effect
        self.key_lvl = key_lvl


class Potion(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell, health_gain, mana_gain, uses):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.health_gain = health_gain
        self.mana_gain = mana_gain
        self.uses = uses


class Posion_Potion(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell,health_stolen,mana_stolen,special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.health_stolen = health_stolen
        self.mana_stolen = mana_stolen
        self.special_effect = special_effect


class Ring(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.special_effect = special_effect
        self.extra_health = extra_health
        self.extra_mana = extra_mana
        self.extra_damage = extra_damage
        self.extra_defence = extra_defence


class Amulet(Item):
    def __init__(self, typee, name, consumable, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.special_effect = special_effect
        self.extra_health = extra_health
        self.extra_mana = extra_mana
        self.extra_damage = extra_damage
        self.extra_defence = extra_defence


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
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, defence):
        super().__init__(typee, name, consumable, price_buy, price_sell)
        self.strength_requirement = strength_requirement
        self.agility_requirement = agility_requirement
        self.defence = defence

    def check_armor(self, player_strength, player_agility,):
        if self.strength_requirement < player_strength and self.agility_requirement < player_agility:
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


class Lance(Weapon):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed, charge_damage, charge_damage_mana_requirement):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed)
        self.charge_damage = charge_damage
        self.charge_damage_mana_requirement = charge_damage_mana_requirement


class ChestPlate(Armor):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, defence, special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, defence)
        self.special_effect = special_effect


class Pants(Armor):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, defence, special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, defence)
        self.special_effect = special_effect


class Shoes(Armor):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, defence, special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, defence)
        self.special_effect = special_effect


class Gloves(Armor):
    def __init__(self, typee, name, consumable, price_buy, price_sell, strength_requirement, defence, special_effect):
        super().__init__(typee, name, consumable, price_buy, price_sell, strength_requirement, defence)
        self.special_effect = special_effect


# speed = co ile sekund atak od momentu kliknienioa przycisku
# template : Sword_blahblah = Sword("sword", "Sword_blahblah", False, 500, 400, 25, 10, 30, 2, 50, 25)
# items = [None, Sword_blahblah, axe_coścoś, itp...]
