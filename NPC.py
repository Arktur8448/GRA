import arcade
import items
import inventory
from races import Friend

class NPC (arcade.Sprite):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None, to_sell=None):
        super().__init__(filename=filename, center_x=pos_x, center_y=pos_y, scale=1.6)
        self.name = name
        self.description = description
        self.level = level
        self.exp_drop = exp_drop
        self.health = health
        self.max_health = self.health
        self.strength = strength
        self.defence = defence
        self.agility = agility
        self.speed = speed
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

    def show_health(self):
        hp = arcade.Text(
            f"HP: {int(self.health)}/{self.max_health}",
            self.center_x - 60,
            self.center_y + 40,
            arcade.color.RED,
            15,
            font_name="Kenney Blocks",
        )
        return hp


class Tradesman(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None, to_sell=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop, to_sell)
    def buy_item(self, item_index, buyer):
        if 0 <= item_index < len(self.to_sell):
            item, price = self.to_sell[item_index]
            if buyer.gold >= price:
                buyer.gold -= price
                buyer.inventory.append(item)
                return f"You bought {item.name} for {price} Gold."
            else:
                return "You don't have enough Gold to buy this item."
        else:
            return "Invalid item index."

    def sell_item(self, item_index, seller):
        item,price = self.to_sell[item_index]
        seller.gold += (price * 0.8)
        seller.inventory.remove(item)


class Smith(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None, to_sell=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop, to_sell)

    def buy_item(self, item_index, buyer):
        if 0 <= item_index < len(self.to_sell):
            item, price = self.to_sell[item_index]
            if buyer.gold >= price:
                buyer.gold -= price
                buyer.inventory.append(item)
                return f"You bought {item.name} for {price} Gold."
            else:
                return "You don't have enough Gold to buy this item."
        else:
            return "Invalid item index."

    def upgrader(self,item,book_effect,book_price,player):
        if player.gold >= book_price:
            player.gold -= book_price
            item.special_effect.append(book_effect)

    def dropupgrade(self,item,book_effect,book_price,player):
        if player.gold >= (book_price * 0.4):
            player.gold -= (book_price * 0.4)
            item.special_effect.remove(book_effect)


class Alchemist(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None, to_sell=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop, to_sell)

    def use_spell(self,player):
        pass

    def buy_item(self, item_index, buyer):
        if 0 <= item_index < len(self.to_sell):
            item, price = self.to_sell[item_index]
            if buyer.gold >= price:
                buyer.gold -= price
                buyer.inventory.append(item)
                return f"You bought {item.name} for {price} Gold."
            else:
                return "You don't have enough Gold to buy this item."
        else:
            return "Invalid item index."


class EnemyShortDistance(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None,armor=None,special_skill=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop)
        self.armor = armor if armor else []
        self.special_skill = special_skill if special_skill else []


class EnemyLongDistance(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None,armor=None,special_skill=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop)
        self.armor = armor if armor else []
        self.special_skill = special_skill if special_skill else []


class HeavyEnemy(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None,armor=None,special_skill=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop)
        self.armor = armor if armor else []
        self.special_skill = special_skill if special_skill else []


class Mage(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None,armor=None,magic=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop,)
        self.armor = armor if armor else []
        self.magic = magic if magic else []

    def use_spell(self,player):
        pass


class Boss(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None,armor=None,act=1):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop)
        self.armor = armor if armor else []
        self.act = act

    def check_act(self,player):
        if player.act == self.act:
            return True
        else:
            return False


class Friends(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=Friend,
                 weapon=None, drop=None,act=1,armor=None):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop)
        self.act = act
        self.armor = armor if armor else []
        #to taki ziutek co daje ci misje na poczatku i on rozpoczyna fabule

    def check_act(self,player):
        if player.act == self.act:
            return True
        else:
            return False


class Cleric(NPC):
    def __init__(self, filename, name, description, pos_x, pos_y, level=1, exp_drop=0, health=1, strength=1, defence=1, agility=1,speed=1, race=None,
                 weapon=None, drop=None,armor=None,special_skill=None,religion=""):
        super().__init__(filename, name, description, pos_x, pos_y, level, exp_drop, health, strength, defence, agility,speed, race,weapon, drop)
        self.armor = armor if armor else []
        self.special_skill = special_skill if special_skill else []
        self.religion = religion



