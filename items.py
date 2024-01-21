import arcade


class Item(arcade.Sprite):
    def __init__(self, sprite_path, description, item_rarity, name, price_buy, price_sell):
        super().__init__(filename=sprite_path, scale=0.5)
        self.description = description
        self.item_rarity = item_rarity
        self.name = name
        self.price_buy = price_buy
        self.price_sell = price_sell


class Food(Item):
    def __init__(self, sprite_path, description, name, item_rarity=0, price_buy=0, price_sell=0, regen_health=0, regen_mana=0, time_regen=0, consumable=True):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell)
        self.regen_health = regen_health
        self.regen_mana = regen_mana
        self.time_regen = time_regen
        self.consumable = consumable
        self.action = [
            ["Eat", self.eat],
            ["Drop", self.drop]
        ]

    def eat(self, player):
        player.health += self.regen_health

    def drop(self):
        pass
        #wyrzucanie itemow

class Upgrader(Item):
    def __init__(self, sprite_path, description, name, item_rarity, price_buy, price_sell, special_effect, lvl_upgrader):
        super().__init__(sprite_path, description, name, item_rarity,  price_buy, price_sell)
        self.special_effect = special_effect if special_effect else []
        self.lvl_upgrader = lvl_upgrader

    def check_lvl(self, player_lvl):
        if player_lvl >= self.lvl_upgrader:
            return True
        else:
            return False


class Book(Upgrader):
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, special_effect = None, lvl_upgrader=1, type_item="Weapon"):
        super().__init__(sprite_path, description, name, item_rarity,  price_buy, price_sell, special_effect, lvl_upgrader)
        self.type_item = type_item


class Ore(Item):
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, mining_lucky=0, lvl_ore=1):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell)
        self.mining_lucky = mining_lucky
        self.lvl_ore = lvl_ore
        self.action = [
            ["Drop", self.drop]
        ]

    def drop(self):
        pass
        #wydupca z equ

    def extralucky(self, lucky_lvl):
        self.mining_lucky *= lucky_lvl

    def check_lvl(self,player_lvl):
        if player_lvl >= self.lvl_ore:
            return True
        else:
            return False


class Key(Item):
    def __init__(self, sprite_path, description, name, price_buy=0, price_sell=0, destination="First Village", key_lvl=1):
        super().__init__(sprite_path, description, name, 0, price_buy, price_sell)
        self.destination = destination
        self.key_lvl = key_lvl
        self.action = [
            ["Drop", self.drop]
        ]

    def drop(self):
        pass
        #WYDUPIA

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
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, health_gain=0, mana_gain=0, stamina_gain=0, strength_gain=0):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell)
        self.health_gain = health_gain
        self.mana_gain = mana_gain
        self.stamina_gain = stamina_gain
        self.strength_gain = strength_gain
        self.action = [
            ["Use", self.use],
            ["Drop", self.drop]
        ]

    def use(self,player):
        player.health += self.health_gain
        player.mana += self.mana_gain
        player.stamina += self.stamina_gain
        player.strength += self.strength_gain

    def drop(self):
        pass
        # wydupia


class Accessories(Item):
    def __init__(self, sprite_path, description,  item_rarity, name, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, extra_stamina, extra_strength, lvl_accessory):
        super().__init__(sprite_path, description, item_rarity, name, price_buy, price_sell)
        self.special_effect = special_effect
        self.extra_health = extra_health
        self.extra_mana = extra_mana
        self.extra_damage = extra_damage
        self.extra_defence = extra_defence
        self.extra_stamina = extra_stamina
        self.extra_strength = extra_strength
        self.lvl_accessory = lvl_accessory

    def check_lvl(self, player_lvl):
        if player_lvl >= self.lvl_accessory:
            return True
        else:
            return False


class Ring(Accessories):
    def __init__(self, sprite_path, description, name,  item_rarity="Common", price_buy=0, price_sell=0, special_effect=0, extra_health=0, extra_mana=0, extra_damage=0, extra_defence=0, extra_stamina=0, extra_strength=0, lvl_accessory=1):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, extra_stamina, extra_strength, lvl_accessory)
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Amulet(Accessories):
    def __init__(self, sprite_path, description, name,  item_rarity="Common", price_buy=0, price_sell=0, special_effect=0, extra_health=0, extra_mana=0, extra_damage=0, extra_defence=0, extra_stamina=0, extra_strength=0, lvl_accessory=1):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, extra_stamina, extra_strength, lvl_accessory)
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia



class Necklace(Accessories):
    def __init__(self, sprite_path, description, name,  item_rarity="Common", price_buy=0, price_sell=0, special_effect=0, extra_health=0, extra_mana=0, extra_damage=0, extra_defence=0, extra_stamina=0, extra_strength=0, lvl_accessory=1):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell, special_effect, extra_health, extra_mana, extra_damage, extra_defence, extra_stamina, extra_strength, lvl_accessory)
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia



class Weapon(Item):
    def __init__(self, sprite_path, description,  item_rarity, name, price_buy, price_sell, strength_requirement, agility_requirement, damage, speed , lvl_weapon):
        super().__init__(sprite_path, description, item_rarity, name, price_buy, price_sell)
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
    def __init__(self, sprite_path, description, name, item_rarity=0, price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0,
                 damage=0, speed=0, charge_damage=0, charge_damage_mana_requirement=0, lvl_weapon=1, special_effect=None):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement,
                         damage, speed, lvl_weapon)
        self.charge_damage = charge_damage
        self.charge_damage_mana_requirement = charge_damage_mana_requirement
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Axe(Weapon):
    def __init__(self, sprite_path, description, name, item_rarity=0, price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0,
                 damage=0, speed=0, charge_damage=0, charge_damage_mana_requirement=0, lvl_weapon=1, special_effect=None):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement,
                         damage, speed, lvl_weapon)
        self.charge_damage = charge_damage
        self.charge_damage_mana_requirement = charge_damage_mana_requirement
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Lance(Weapon):
    def __init__(self, sprite_path, description, name, item_rarity=0, price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0,
                 damage=0, speed=0, charge_damage=0, charge_damage_mana_requirement=0, lvl_weapon=1, special_effect=None):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement,
                         damage, speed, lvl_weapon)
        self.charge_damage = charge_damage
        self.charge_damage_mana_requirement = charge_damage_mana_requirement
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Armor(Item):
    def __init__(self, sprite_path, description, name, item_rarity, price_buy, price_sell, strength_requirement, agility_requirement,
                 defence, lvl_armor):
        super().__init__(sprite_path, description, name, item_rarity, price_buy, price_sell)
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
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0, defence=0, special_effect=None,
                 lvl_armor=1):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class ChestPlate(Armor):
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0, defence=0, special_effect=None,
                 lvl_armor=1):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Gloves(Armor):
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0, defence=0, special_effect=None,
                 lvl_armor=1):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Pants(Armor):
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0, defence=0, special_effect=None,
                 lvl_armor=1):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia


class Shoes(Armor):
    def __init__(self, sprite_path, description, name, item_rarity="Common", price_buy=0, price_sell=0, strength_requirement=0, agility_requirement=0, defence=0, special_effect=None,
                 lvl_armor=1):
        super().__init__(sprite_path, description, name, item_rarity,price_buy, price_sell, strength_requirement, agility_requirement, defence, lvl_armor)
        self.special_effect = special_effect if special_effect else []
        self.action = [
            ["Equip", self.equip],
            ["Drop", self.drop]
        ]

    def equip(self):
        pass
        # zakladnie

    def drop(self):
        pass
        # wydupia



# speed = co ile sekund atak od momentu kliknienioa przycisku
# template : Sword_blahblah = Sword("sword", "Sword_blahblah", False, 500, 400, 25, 10, 30, 2, 50, 25)
# items = [None, Sword_blahblah, axe_coścoś, itp...]

items = [
    None,
    Food("sprites/player/Player.png", "", "Apple", 1, 10, 5, 2, 0, 3, True),
    Food("sprites/player/Player.png", "", "Bread", 2, 20, 10, 3, 0, 3, True),
    Food("sprites/player/Player.png", "", "Cheese", 4, 25, 20, 1, 1, 5, True),
    Food("sprites/player/Player.png", "", "Soup", 3, 20, 15, 2, 2, 2, True),
    Food("sprites/player/Player.png", "", "Steak", 5, 40, 35, 5, 1, 2, True),
    Food("sprites/player/Player.png", "", "Salad", 3, 25, 20, 2, 3, 2, True),
    Food("sprites/player/Player.png", "", "Chocolate Bar", 6, 15, 10, 3, 3, 3, True),
    Food("sprites/player/Player.png", "", "Fruit Smoothie", 3, 20, 15, 2, 1, 3, True),
    Food("sprites/player/Player.png", "", "Carrot", 1, 8, 6, 2, 0, 2, True),
    Food("sprites/player/Player.png", "", "Golden Apple", 7, 50, 40, 3, 3, 5, True),

    Key("sprites/player/Player.png", "", "King's Room Key", 200, 150, "King's Room", 1),
    Key("sprites/player/Player.png", "", "Boss's Room Key", 200, 150, "Boss's Room Key", 1),
    Key("sprites/player/Player.png", "", "Mystical Key", 200, 150, "Mystical Door", 1),
    Key("sprites/player/Player.png", "", "Ancient Key", 200, 150, "Ancient Temple Door", 1),
    Key("sprites/player/Player.png", "", "Golden Key", 200, 150, "Golden Room", 1),

    Ore("sprites/player/Player.png", "", "Iron", "Common", 25, 20, 2, 1),
    Ore("sprites/player/Player.png", "", "Gold", "Rare", 40, 35, 3, 2),
    Ore("sprites/player/Player.png", "", "Copper", "Common", 20, 15, 2, 1),
    Ore("sprites/player/Player.png", "", "Diamond", "Rare", 50, 45, 4, 3),
    Ore("sprites/player/Player.png", "", "Ruby", "Ultra Rare", 75, 60, 5, 3),
    Ore("sprites/player/Player.png", "", "Emerald", "Rare", 60, 50, 4, 3),

    Book("sprites/player/Player.png", " ", "Spellbook of Fire", "Rare", 200, 150, [None, "fire resistant"], 2, "Armor"),
    Book("sprites/player/Player.png", " ", "Spellbook of Durability", "Rare", 200, 150, [None, "durability"], 2, "Armor"),
    Book("sprites/player/Player.png", " ", "Spellbook of Thorns", "Rare", 200, 150, [None, "thorns"], 3, "Armor"),
    Book("sprites/player/Player.png", " ", "Spellbook of Speed", "Rare", 200, 150, [None, "speed"], 3, "Armor"),
    Book("sprites/player/Player.png", " ", "Spellbook of Fire Aspect", "Rare", 200, 150, [None, "fire aspect"], 2, "Weapon"),
    Book("sprites/player/Player.png", " ", "Spellbook of Knockback", "Rare", 200, 150, [None, "knockback"], 3, "Weapon"),
    Book("sprites/player/Player.png", " ", "Spellbook of Sharpness", "Rare", 200, 150, [None, "sharpness"], 3, "Weapon"),
    Book("sprites/player/Player.png", " ", "Spellbook of Looting", "Rare", 200, 150, [None, "looking"], 3,
         "Weapon"),

    Potion("sprites/player/Player.png", " ", "Small Health Potion", "Common", 25, 20, 5, 0, 0, 0,),
    Potion("sprites/player/Player.png", " ", "Big Health Potion", "Common", 50, 40, 10, 0, 0, 0),
    Potion("sprites/player/Player.png", " ", "Small Mana Potion", "Common", 25, 20, 0, 5, 0, 0),
    Potion("sprites/player/Player.png", " ", "Big Mana Potion", "Common", 50, 40, 0, 10, 0, 0),
    Potion("sprites/player/Player.png", " ", "Strength Potion", "Common", 60, 50, 0, 0, 0, 10),
    Potion("sprites/player/Player.png", " ", "Stamina Potion", "Common", 75, 60, 0, 0, 10, 0),
    Potion("sprites/player/Player.png", " ", "Energy Drink", "Common", 80, 70, 0, 0, 10, 10),

    Ring("sprites/player/Player.png", " ", "King's Ring", "Epic", 0, 250, 10, 10, 5, 3, lvl_accessory=1)
 ]














