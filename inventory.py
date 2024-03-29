import arcade
import items
import time
import player
import copy

SCREEN_WIDTH = 992
SCREEN_HEIGHT = 572


class Slot(arcade.Sprite):  # Slot jest jednocześnie spritem i obiektem z funckjami i wartościami
    def __init__(self, slot_sprite, center_x, center_y, scale, type_of_item=None, held_item=None):
        super().__init__(slot_sprite, center_x=center_x, center_y=center_y, scale=scale)
        self.type_of_item = type_of_item
        if self.type_of_item is not None:
            if type(held_item) is self.type_of_item:
                self.held_item = held_item
            else:
                self.held_item = None
        else:
            self.held_item = held_item

        self.can_show_item = True

    def show_item(self):
        if self.held_item is not None:
            if self.can_show_item:
                self.held_item.center_x = self.center_x
                self.held_item.center_y = self.center_y
            self.held_item.draw()


class InventoryView(arcade.View):
    def __init__(self, player_object, game_view):
        super().__init__()
        self.playerObject = player_object
        self.gameView = game_view
        self.scene = None

        self.camera = None

        self.row_count = 10
        self.coulum_count = 9

        self.hold_item = None
        self.hold_item_slot = None

        self.hold_item_slot_last = None

        self.playerObjectCopy = copy.deepcopy(self.playerObject)
        self.playerInventory = [None] * 150
        self.check_once = 0

    def on_show_view(self):
        arcade.set_background_color((42, 42, 42))
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Slots")
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Exit")
        for r in range(1, self.row_count + 1):
            for c in range(1, self.coulum_count + 1):
                self.scene.add_sprite("Slots", Slot("sprites/inventory/slot.png",
                                                    SCREEN_WIDTH / 2 + 50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))

        self.scene.add_sprite("Player", Slot("sprites/player/Idle_Down.png",
                                             250,
                                             SCREEN_HEIGHT / 1.5,
                                             5))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/hat.png",
                                            249,
                                            SCREEN_HEIGHT - 60,
                                            1.5, items.Hat))
        x = 150
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                x,
                                                SCREEN_HEIGHT - 132,
                                                1, items.Ring))
            x += 195
        del x
        self.scene.add_sprite("Slots", Slot("sprites/inventory/chest.png",
                                            center_x=150,
                                            center_y=SCREEN_HEIGHT - 178,
                                            scale=1.5,
                                            type_of_item=items.ChestPlate))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/gloves.png",
                                            center_x=345,
                                            center_y=SCREEN_HEIGHT - 178,
                                            scale=1.5,
                                            type_of_item=items.Gloves))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/pants.png",
                                            center_x=150,
                                            center_y=SCREEN_HEIGHT - 230,
                                            scale=1.5,
                                            type_of_item=items.Pants))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/slot.png",
                                            center_x=345,
                                            center_y=SCREEN_HEIGHT - 230,
                                            scale=1.5,
                                            type_of_item=items.Shoes))
        x = 125
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 274,
                                                scale=1,
                                                type_of_item=items.Ring))
            x += 48
        del x
        x = 320
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 274,
                                                scale=1,
                                                type_of_item=items.Ring))
            x += 48
        del x
        x = 174
        for i in range(0, 4):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/weapon.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 322,
                                                scale=1.5))
            x += 52
        del x
        x = 122
        for i in range(0, 6):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/potions.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 390,
                                                scale=1.5))
            x += 52
        del x
        x = 197
        for i in range(0, 3):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/slot.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 440,
                                                scale=1.5))
            x += 52
        del x
        self.scene.add_sprite("Exit", Slot("sprites/inventory/slot.png",
                                            center_x=24,
                                            center_y=SCREEN_HEIGHT-24,
                                            scale=1))

        self.load_inventory()

    def move_item(self, form_slot_index, to_slot_index):
        tmp = self.scene.get_sprite_list("Slots")[to_slot_index].held_item
        self.scene.get_sprite_list("Slots")[to_slot_index].held_item = self.scene.get_sprite_list("Slots")[
            form_slot_index].held_item
        self.scene.get_sprite_list("Slots")[form_slot_index].held_item = tmp

    def delete_item(self, slot_index):
        self.scene.get_sprite_list("Slots")[slot_index].held_item = None

    def add_item(self, item):
        # self.playerInventory.append(items.Ring("sprites/inventory/ring.png", "good", "hat", "Common", 0, 0, 0, 0, 10))
        for i in range(0, len(self.playerInventory)):
            if self.playerInventory[i] is None:
                self.playerInventory[i] = item
                self.load_inventory()
                break

    def load_inventory(self):
        for i in range(0, len(self.scene.get_sprite_list("Slots"))):
            self.scene.get_sprite_list("Slots")[i].held_item = self.playerInventory[i]
            if self.playerInventory[i] is not None:
                print(i, end=" ")
                print(self.playerInventory[i])
            self.check_once = 1

    def check_equipped(self):
        self.playerObject.defence = self.playerObjectCopy.defence
        od = 90
        do = 101
        for s in self.scene.get_sprite_list("Slots")[od:do]:
            if s.held_item is not None:
                if type(s.held_item) is items.Hat or type(s.held_item) is items.ChestPlate or type(
                        s.held_item) is items.Pants or type(s.held_item) is items.Shoes:
                    self.playerObject.defence += s.held_item.defence
                elif type(s.held_item) is items.Ring or type(s.held_item) is items.Amulet or type(
                        s.held_item) is items.Necklace:
                    self.playerObject.health += s.held_item.extra_health
                    self.playerObject.mana += s.held_item.extra_mana
                    # self.playerObject.damage = self.playerObjectCopy.damage + s.held_item.extra_damage
                    self.playerObject.defence += s.held_item.extra_defence
                    self.playerObject.stamina += s.held_item.extra_stamina
                    self.playerObject.strength += s.held_item.extra_strength

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw(pixelated=True)
        for s in self.scene.get_sprite_list("Slots"):
            s.show_item()

    def on_update(self, delta_time):
        if arcade.key.I in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.I]
            self.gameView.camera.use()
            self.window.show_view(self.gameView)
            self.load_inventory()
        if arcade.key.A in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.A]
            self.add_item(items.Ring("sprites/inventory/ring.png", "good", "hat", "Common", 0, 0, 0, 0, 10))
        if self.check_once == 0:
            self.load_inventory()
        self.check_equipped()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)):
                    self.hold_item = s.held_item
                    self.hold_item_slot = s
                    self.hold_item_slot.can_show_item = False
                    self.hold_item_slot_last = s.held_item
            for s in self.scene.get_sprite_list("Exit"):
                if s.collides_with_point((x, y)):
                    self.gameView.camera.use()
                    self.window.show_view(self.gameView)
                    self.load_inventory()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float,
                      _buttons: int, _modifiers: int):
        if self.hold_item:
            self.hold_item.position = x, y

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)) and s is not self.hold_item_slot and self.hold_item:
                    try:
                        if s.held_item is None:
                            if s.type_of_item is type(self.hold_item) or s.type_of_item is None:
                                self.playerInventory[self.scene.get_sprite_list("Slots").index(s)] = self.hold_item
                                s.held_item = self.hold_item
                                self.playerInventory[self.scene.get_sprite_list("Slots").index(self.hold_item_slot)] = None
                                self.hold_item_slot = None
                                self.load_inventory()
                                break
                        else:
                            if s.type_of_item is type(self.hold_item) or s.type_of_item is None:
                                tmp = s.held_item
                                s.held_item = self.hold_item
                                self.hold_item_slot.held_item = tmp
                                break
                    except:
                        self.hold_item_slot_last = self.hold_item

            if self.hold_item:
                try:
                    self.hold_item = None
                    self.hold_item_slot.can_show_item = True
                except:
                    pass
                if self.hold_item_slot is not None:
                    self.hold_item_slot_last = self.hold_item_slot
                self.hold_item_slot = None


class BlackSmithView(arcade.View):
    def __init__(self, player_object, game_view):
        super().__init__()
        self.playerObject = player_object
        self.gameView = game_view
        self.scene = None

        self.camera = None

        self.row_count = 10
        self.coulum_count = 9

        self.hold_item = None
        self.hold_item_slot = None

        self.hold_item_slot_last = None

        self.playerObjectCopy = copy.deepcopy(self.playerObject)
        self.page = 2
        self.playerInventory = [None] * 150
        self.playerInventory[0] = items.Ring("sprites/inventory/chest.png", "good", "hat", "Common", 10, 0, 0, 0,10)
        self.check_once = 0
        self.blacksmithEnchant = [None] * 3
        self.blacksmithDeEnchant = [None] * 2
        self.blacksmithInventory = [None] * 150

    def on_show_view(self):
        arcade.set_background_color((42, 42, 42))
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Slots")
        self.scene.add_sprite_list("Blacksmith1")
        self.scene.add_sprite_list("Blacksmith2")
        self.scene.add_sprite_list("Blacksmith3")
        self.scene.add_sprite_list("Pager")
        self.scene.add_sprite_list("Exit")
        for r in range(1, self.row_count + 1):
            for c in range(1, self.coulum_count + 1):
                self.scene.add_sprite("Slots", Slot("sprites/inventory/slot.png",
                                                    SCREEN_WIDTH / 2 + 50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))
        # page 1
        self.scene.add_sprite("Blacksmith1", Slot("sprites/inventory/weapon.png",
                                                  100,
                                                  264,
                                                  1.5))
        self.scene.add_sprite("Blacksmith1", Slot("sprites/inventory/weapon.png",
                                                  200,
                                                  264,
                                                  1.5))
        self.scene.add_sprite("Blacksmith1", Slot("sprites/inventory/weapon.png",
                                                  300,
                                                  264,
                                                  2))
        # page 2
        self.scene.add_sprite("Blacksmith2", Slot("sprites/inventory/weapon.png",
                                                  150,
                                                  264,
                                                  1.5))
        self.scene.add_sprite("Blacksmith2", Slot("sprites/inventory/weapon.png",
                                                  250,
                                                  264,
                                                  2))
        # page 3
        for r in range(1, 9):
            for c in range(1, 10):
                self.scene.add_sprite("Blacksmith3", Slot("sprites/inventory/slot.png",
                                                    50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))
        for s in range(1, 4):
            self.scene.add_sprite("Pager", Slot("sprites/inventory/hat.png",
                                                175+50*s,
                                                50,
                                                1))
        self.scene.add_sprite("Exit", Slot("sprites/inventory/slot.png",
                                           center_x=24,
                                           center_y=SCREEN_HEIGHT - 24,
                                           scale=1))

        self.load_inventory()

    def move_item(self, form_slot_index, to_slot_index):
        tmp = self.scene.get_sprite_list("Slots")[to_slot_index].held_item
        self.scene.get_sprite_list("Slots")[to_slot_index].held_item = self.scene.get_sprite_list("Slots")[
            form_slot_index].held_item
        self.scene.get_sprite_list("Slots")[form_slot_index].held_item = tmp

    def delete_item(self, slot_index):
        self.scene.get_sprite_list("Slots")[slot_index].held_item = None

    def add_item(self, item):
        # self.playerInventory.append(items.Ring("sprites/inventory/ring.png", "good", "hat", "Common", 0, 0, 0, 0, 10))
        for i in range(0, len(self.playerInventory)):
            if self.playerInventory[i] is None:
                self.playerInventory[i] = item
                self.load_inventory()
                break

    def load_inventory(self):
        for i in range(0, len(self.scene.get_sprite_list("Slots"))):
            self.scene.get_sprite_list("Slots")[i].held_item = self.playerInventory[i]
        for i in range(0, len(self.scene.get_sprite_list("Blacksmith1"))):
            self.scene.get_sprite_list("Blacksmith1")[i].held_item = self.blacksmithEnchant[i]
        for i in range(0, len(self.scene.get_sprite_list("Blacksmith2"))):
            self.scene.get_sprite_list("Blacksmith2")[i].held_item = self.blacksmithDeEnchant[i]
        for i in range(0, len(self.scene.get_sprite_list("Blacksmith3"))):
            self.scene.get_sprite_list("Blacksmith3")[i].held_item = self.blacksmithInventory[i]
        self.check_once = 1

    def on_draw(self):
        self.clear()
        self.camera.use()
        tab = ["Slots", "Pager", "Exit"]
        if self.page == 1:
            tab.append("Blacksmith1")
            for s in self.scene.get_sprite_list("Blacksmith2"):
                s.held_item = None
            for s in self.scene.get_sprite_list("Blacksmith3"):
                s.held_item = None
        if self.page == 2:
            tab.append("Blacksmith2")
            for s in self.scene.get_sprite_list("Blacksmith1"):
                s.held_item = None
            for s in self.scene.get_sprite_list("Blacksmith3"):
                s.held_item = None
        if self.page == 3:
            tab.append("Blacksmith3")
            for s in self.scene.get_sprite_list("Blacksmith1"):
                s.held_item = None
            for s in self.scene.get_sprite_list("Blacksmith2"):
                s.held_item = None
        self.scene.draw(names=tab, pixelated=True)
        for s in self.scene.get_sprite_list("Slots"):
            s.show_item()
        for s in self.scene.get_sprite_list("Blacksmith1"):
            s.show_item()
        for s in self.scene.get_sprite_list("Blacksmith2"):
            s.show_item()
        for s in self.scene.get_sprite_list("Blacksmith3"):
            s.show_item()

    def on_update(self, delta_time):
        if arcade.key.I in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.I]
            self.gameView.camera.use()
            self.window.show_view(self.gameView)
            self.load_inventory()
        if self.check_once == 0:
            self.load_inventory()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)):
                    self.hold_item = s.held_item
                    self.hold_item_slot = s
                    self.hold_item_slot.can_show_item = False
                    self.hold_item_slot_last = s.held_item
            for s in self.scene.get_sprite_list("Pager"):
                if s.collides_with_point((x, y)):
                    if s is self.scene.get_sprite_list("Pager")[0]:
                        self.page = 1
                        self.load_inventory()
                    elif s is self.scene.get_sprite_list("Pager")[1]:
                        self.page = 2
                        self.load_inventory()
                    elif s is self.scene.get_sprite_list("Pager")[2]:
                        self.page = 3
                        self.load_inventory()
            for s in self.scene.get_sprite_list("Exit"):
                if s.collides_with_point((x, y)):
                    self.gameView.camera.use()
                    self.window.show_view(self.gameView)
                    self.load_inventory()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float,
                      _buttons: int, _modifiers: int):
        if self.hold_item:
            self.hold_item.position = x, y

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)) and s is not self.hold_item_slot and self.hold_item:
                    try:
                        if s.held_item is None:
                            if s.type_of_item is type(self.hold_item) or s.type_of_item is None:
                                self.playerInventory[self.scene.get_sprite_list("Slots").index(s)] = self.hold_item
                                s.held_item = self.hold_item
                                self.playerInventory[
                                    self.scene.get_sprite_list("Slots").index(self.hold_item_slot)] = None
                                self.hold_item_slot = None
                                self.load_inventory()
                                break
                        else:
                            if s.type_of_item is type(self.hold_item) or s.type_of_item is None:
                                tmp = s.held_item
                                s.held_item = self.hold_item
                                self.hold_item_slot.held_item = tmp
                                break
                    except:
                        self.hold_item_slot_last = self.hold_item

            if self.hold_item:
                try:
                    self.hold_item = None
                    self.hold_item_slot.can_show_item = True
                except:
                    pass
                if self.hold_item_slot is not None:
                    self.hold_item_slot_last = self.hold_item_slot
                self.hold_item_slot = None


class ShopView(arcade.View):
    def __init__(self, player_object, game_view):
        super().__init__()
        self.playerObject = player_object
        self.gameView = game_view
        self.scene = None

        self.camera = None

        self.row_count = 10
        self.coulum_count = 9

        self.hold_item = None
        self.hold_item_slot = None

        self.hold_item_slot_last = None

        self.playerObjectCopy = copy.deepcopy(self.playerObject)
        self.page = 1
        self.playerInventory = [None] * 150
        self.playerInventory[0] = items.Ring("sprites/inventory/chest.png", "good", "hat", "Common", 10, 0, 0, 0,10)
        self.shop_inventory1 = [None] * 150
        self.shop_inventory1[0] = items.Ring("sprites/inventory/ring.png", "good", "hat", "Common", 10, 110, 0, 0,10)
        self.shop_inventory2 = [None] * 150
        self.shop_inventory2[1] = items.Ring("sprites/inventory/ring.png", "good", "hat", "Common", 10, 110, 0, 0, 10)
        self.check_once = 0

    def on_show_view(self):
        arcade.set_background_color((42, 42, 42))
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Slots")
        self.scene.add_sprite_list("Shop1")
        self.scene.add_sprite_list("Shop2")
        self.scene.add_sprite_list("Pager")
        self.scene.add_sprite_list("Exit")
        for r in range(1, self.row_count + 1):
            for c in range(1, self.coulum_count + 1):
                self.scene.add_sprite("Slots", Slot("sprites/inventory/slot.png",
                                                    SCREEN_WIDTH / 2 + 50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))
        # page 1
        for r in range(1, 9):
            for c in range(1, 10):
                self.scene.add_sprite("Shop1", Slot("sprites/inventory/slot.png",
                                                    50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))
        # page 2
        for r in range(1, 9):
            for c in range(1, 10):
                self.scene.add_sprite("Shop2", Slot("sprites/inventory/slot.png",
                                                    50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))
        for s in range(1, 3):
            self.scene.add_sprite("Pager", Slot("sprites/inventory/hat.png",
                                                175+50*s,
                                                50,
                                                1))
        self.scene.add_sprite("Exit", Slot("sprites/inventory/slot.png",
                                           center_x=24,
                                           center_y=SCREEN_HEIGHT - 24,
                                           scale=1))

        self.load_inventory()

    # def move_item(self, form_slot_index, to_slot_index):
    #     tmp = self.scene.get_sprite_list("Slots")[to_slot_index].held_item
    #     self.scene.get_sprite_list("Slots")[to_slot_index].held_item = self.scene.get_sprite_list("Slots")[
    #         form_slot_index].held_item
    #     self.scene.get_sprite_list("Slots")[form_slot_index].held_item = tmp

    def delete_item(self, slot_index):
        self.scene.get_sprite_list("Slots")[slot_index].held_item = None

    def load_inventory(self):
        for i in range(0, len(self.scene.get_sprite_list("Slots"))):
            self.scene.get_sprite_list("Slots")[i].held_item = self.playerInventory[i]
            if self.playerInventory[i] is not None:
                print(i, end=" ")
                print(self.playerInventory[i])
        for i in range(0, len(self.scene.get_sprite_list("Shop1"))):
            self.scene.get_sprite_list("Shop1")[i].held_item = self.shop_inventory1[i]
            if self.shop_inventory1[i] is not None:
                print(i, end=" ")
                print(self.shop_inventory1[i])
        for i in range(0, len(self.scene.get_sprite_list("Shop2"))):
            self.scene.get_sprite_list("Shop2")[i].held_item = self.shop_inventory2[i]
            if self.shop_inventory2[i] is not None:
                print(i, end=" ")
                print(self.shop_inventory2[i])
        self.check_once = 1

    def on_draw(self):
        self.clear()
        self.camera.use()
        tab = ["Slots", "Pager", "Exit"]
        if self.page == 1:
            tab.append("Shop1")
            for s in self.scene.get_sprite_list("Shop2"):
                s.held_item = None
        if self.page == 2:
            tab.append("Shop2")
            for s in self.scene.get_sprite_list("Shop1"):
                s.held_item = None
        self.scene.draw(names=tab, pixelated=True)
        for s in self.scene.get_sprite_list("Slots"):
            s.show_item()
        for s in self.scene.get_sprite_list("Shop1"):
            s.show_item()
        for s in self.scene.get_sprite_list("Shop2"):
            s.show_item()

    def on_update(self, delta_time):
        if arcade.key.I in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.I]
            self.gameView.camera.use()
            self.window.show_view(self.gameView)
            self.load_inventory()
        if arcade.key.A in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.A]
            if self.page == 1:
                self.page = 2
            else:
                self.page = 1
            self.load_inventory()
            # print("lol")
            # self.add_item(items.Ring("sprites/inventory/ring.png", "good", "hat", "Common", 0, 0, 0, 0, 10))
        if self.check_once == 0:
            self.load_inventory()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)):
                    self.hold_item = s.held_item
                    self.hold_item_slot = s
                    self.hold_item_slot.can_show_item = False
                    self.hold_item_slot_last = s.held_item
            for s in self.scene.get_sprite_list("Shop1"):
                if s.collides_with_point((x, y)):
                    try:
                        if self.playerObject.gold >= s.held_item.price_buy:
                            for i in range(0, len(self.playerInventory)):
                                if self.playerInventory[i] is None:
                                    self.playerObject.gold -= s.held_item.price_buy
                                    self.playerInventory[i] = s.held_item
                                    self.load_inventory()
                                    break
                    except:
                        pass
            for s in self.scene.get_sprite_list("Shop2"):
                if s.collides_with_point((x, y)):
                    try:
                        if self.playerObject.gold >= s.held_item.price_buy:
                            # self.playerObject.gold -= s.held_item.price_buy
                            # self.hold_item = s.held_item
                            # self.hold_item_slot = s
                            # self.hold_item_slot.can_show_item = False
                            # self.hold_item_slot_last = s.held_item
                            # ^ jest upo i jak się upusci przed eq to item się dezintegruje więc zrobiłem że po kliknięciu jest buy
                            for i in range(0, len(self.playerInventory)):
                                if self.playerInventory[i] is None:
                                    self.playerObject.gold -= s.held_item.price_buy
                                    self.playerInventory[i] = s.held_item
                                    self.load_inventory()
                                    break
                    except:
                        pass
            for s in self.scene.get_sprite_list("Pager"):
                if s.collides_with_point((x, y)):
                    if s is self.scene.get_sprite_list("Pager")[0]:
                        self.page = 1
                        self.load_inventory()
                    elif s is self.scene.get_sprite_list("Pager")[1]:
                        self.page = 2
                        self.load_inventory()
            for s in self.scene.get_sprite_list("Exit"):
                if s.collides_with_point((x, y)):
                    self.gameView.camera.use()
                    self.window.show_view(self.gameView)
                    self.load_inventory()
            print(self.playerObject.gold)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float,
                      _buttons: int, _modifiers: int):
        if self.hold_item:
            self.hold_item.position = x, y

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)) and s is not self.hold_item_slot and self.hold_item:
                    try:
                        if s.held_item is None:
                            if s.type_of_item is type(self.hold_item) or s.type_of_item is None:
                                self.playerInventory[self.scene.get_sprite_list("Slots").index(s)] = self.hold_item
                                s.held_item = self.hold_item
                                self.playerInventory[
                                    self.scene.get_sprite_list("Slots").index(self.hold_item_slot)] = None
                                self.hold_item_slot = None
                                self.load_inventory()
                                break
                        else:
                            if s.type_of_item is type(self.hold_item) or s.type_of_item is None:
                                tmp = s.held_item
                                s.held_item = self.hold_item
                                self.hold_item_slot.held_item = tmp
                                break
                    except:
                        self.hold_item_slot_last = self.hold_item
            # for s in self.scene.get_sprite_list("Shop1"):
            #     if s.collides_with_point((x, y)) and s is not self.hold_item_slot and self.hold_item:
            #         self.playerObject.gold += self.hold_item.price_sell
            #         self.hold_item_slot = None
            #         print("sprzedane")
            #         self.hold_item = None
            #         self.hold_item_slot_last = None

            if self.hold_item:
                try:
                    self.hold_item = None
                    self.hold_item_slot.can_show_item = True
                except:
                    pass
                if self.hold_item_slot is not None:
                    self.hold_item_slot_last = self.hold_item_slot
                self.hold_item_slot = None