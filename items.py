class Item:
    def __init__(self, sprite_path, description, item_rarity, name, price_buy, price_sell):
        self.sprite_path = sprite_path
        self.description = description
        self.item_rarity = item_rarity
        self.name = name
        self.price_buy = price_buy
        self.price_sell = price_sell


class Food(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, level_of_fullness, consumable):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.level_of_fullness = level_of_fullness
        self.consumable = consumable

    def check_fullness(self, player_fullness):
        if player_fullness > 0:
            return True
        else:
            return False


class WeaponUpgrader(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, type_weapon, special_effect):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.type_weapon = type_weapon
        self.special_effect = special_effect


class ArmorUpgrader(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, type_armor, special_effect):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.type_armor = type_armor
        self.special_effect = special_effect


class Ore(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, mining_lucky):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.mining_lucky = mining_lucky

    def extralucky(self, lucky_lvl):
        self.mining_lucky *= lucky_lvl


class Key(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, destination, special_effect, key_lvl):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.destination = destination
        self.special_effect = special_effect
        self.key_lvl = key_lvl

    def check_lvl(self, player_lvl):
        if player_lvl == self.key_lvl:
            return True
        else:
            return False

    # ten ziut sprawdza czy lewel gracza jest git z uzyciem klucza
    def check_destination(self, key_task):
        if key_task == self.destination:
            return True
        else:
            return False
    # to taki ziut do sprawdzania czy dany klucz jest do danej rzczey np do skrzynki albo drzwi


class Potion(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, health_gain, mana_gain, uses):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.health_gain = health_gain
        self.mana_gain = mana_gain
        self.uses = uses


class Accessories(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.special_effect = special_effect
        self.extra_health = extra_health
        self.extra_mana = extra_mana
        self.extra_damage = extra_damage
        self.extra_defence = extra_defence
        self.lvl_accessory = lvl_accessory

    def check_lvl(self, player_lvl):
        if player_lvl >= self.lvl_accessory:
            return True
        else:
            return False


class Ring(Accessories):
    def __init__(self, item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory):
        super().__init__(item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory)


class Amulet(Accessories):
    def __init__(self, item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory):
        super().__init__(item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory)


class Necklace(Accessories):
    def __init__(self, item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory):
        super().__init__(item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, lvl_accessory)


class Weapon(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed , lvl_weapon):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.strength_requirement = strength_requirement
        self.agility_requirement = agility_requirement
        self.damage = damage
        self.speed = speed
        self.lvl_weapon = lvl_weapon

    def check_weapon(self, player_strength, player_agility):
        if self.strength_requirement < player_strength and self.agility_requirement < player_agility:
            return True
        else:
            return False

    def upgrade(self, upgrade_level):
        self.damage += upgrade_level
        self.speed += upgrade_level

    def check_lvl(self, player_lvl):
        if player_lvl >= self.lvl_weapon:
            return True
        else:
            return False


class Sword(Weapon):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                 damage, speed, slash_damage, slash_damage_mana_requirement, lvl_weapon):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                         damage, speed, lvl_weapon)
        self.slash_damage = slash_damage
        self.slash_damage_mana_requirement = slash_damage_mana_requirement


class Axe(Weapon):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                 damage, speed, chop_damage, chop_damage_mana_requirement, lvl_weapon):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                         damage, speed, lvl_weapon)
        self.chop_damage = chop_damage
        self.chop_damage_mana_requirement = chop_damage_mana_requirement


class Lance(Weapon):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                 damage, speed, charge_damage, charge_damage_mana_requirement, lvl_weapon):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                         damage, speed, lvl_weapon)
        self.charge_damage = charge_damage
        self.charge_damage_mana_requirement = charge_damage_mana_requirement


class Armor(Item):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement,
                 defence, lvl_armor):
        super().__init__(item_rarity, name, price_buy, price_sell)
        self.strength_requirement = strength_requirement
        self.agility_requirement = agility_requirement
        self.defence = defence
        self.lvl_armor = lvl_armor

    def check_armor(self, player_strength, player_agility):
        if self.strength_requirement < player_strength and self.agility_requirement < player_agility:
            return True
        else:
            return False

    def upgrade(self, upgrade_level):
        self.defence *= upgrade_level

    def check_lvl(self, player_lvl):
        if player_lvl >= self.lvl_armor:
            return True
        else:
            return False


class Hat(Armor):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, special_effect,
                 lvl_armor):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect


class ChestPlate(Armor):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, special_effect,
                 lvl_armor):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect


class Pants(Armor):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, special_effect,
                 lvl_armor):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect


class Shoes(Armor):
    def __init__(self, item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, special_effect,
                 lvl_armor):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect


class Gloves(Armor):
    def __init__(self, name, item_rarity="Common", price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0, defence=0, special_effect=[],
                 lvl_armor=1):
        super().__init__(item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect


# speed = co ile sekund atak od momentu kliknienioa przycisku
# template : Sword_blahblah = Sword("sword", "Sword_blahblah", False, 500, 400, 25, 10, 30, 2, 50, 25)
# items = [None, Sword_blahblah, axe_coścoś, itp...]










