import arcade
import items
import time
import player

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

    def on_show_view(self):
        arcade.set_background_color((42, 42, 42))
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Slots")
        self.scene.add_sprite_list("Player")
        for r in range(1, self.row_count + 1):
            for c in range(1, self.coulum_count + 1):
                self.scene.add_sprite("Slots", Slot("sprites/inventory/Slot.png",
                                                    SCREEN_WIDTH / 2 + 50 * c,
                                                    SCREEN_HEIGHT - 25 - 50 * r,
                                                    1.5))

        self.scene.add_sprite("Player", Slot("sprites/player/player_base.png",
                                             250,
                                             SCREEN_HEIGHT / 1.5,
                                             5))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/hat.png",
                                            249,
                                            SCREEN_HEIGHT - 60,
                                            1.5, "hat"))
        x = 150
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                x,
                                                SCREEN_HEIGHT - 132,
                                                1, "chest"))
            x += 195
        del x
        self.scene.add_sprite("Slots", Slot("sprites/inventory/chest.png",
                                            center_x=150,
                                            center_y=SCREEN_HEIGHT - 178,
                                            scale=1.5))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/gloves.png",
                                            center_x=345,
                                            center_y=SCREEN_HEIGHT - 178,
                                            scale=1.5))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/pants.png",
                                            center_x=150,
                                            center_y=SCREEN_HEIGHT - 230,
                                            scale=1.5))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/Slot.png",
                                            center_x=345,
                                            center_y=SCREEN_HEIGHT - 230,
                                            scale=1.5))
        x = 125
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 274,
                                                scale=1))
            x += 48
        del x
        x = 320
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 274,
                                                scale=1))
            x += 48
        del x
        x = 174
        for i in range(0, 4):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/Slot.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 322,
                                                scale=1.5))
            x += 52
        del x
        x = 122
        for i in range(0, 6):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/Slot.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 390,
                                                scale=1.5))
            x += 52
        del x
        x = 197
        for i in range(0, 3):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/Slot.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 440,
                                                scale=1.5))
            x += 52
        del x

        self.scene.get_sprite_list("Slots")[0].held_item = items.Hat("sprites/inventory/hat.png", "good", "hat", "Common", 0, 0, 0, 0, 10) # name narazie używam do funkcji equip_item ale to tylko chwilowo, jest do zmienienia

    def move_item(self, form_slot_index, to_slot_index):
        tmp = self.scene.get_sprite_list("Slots")[to_slot_index].held_item
        self.scene.get_sprite_list("Slots")[to_slot_index].held_item = self.scene.get_sprite_list("Slots")[
            form_slot_index].held_item
        self.scene.get_sprite_list("Slots")[form_slot_index].held_item = tmp

    def delete_item(self, slot_index):
        self.scene.get_sprite_list("Slots")[slot_index].held_item = None

    def add_item(self, slot_index):
        self.scene.get_sprite_list("Slots")[slot_index].held_item = items.Hat("sprites/inventory/hat.png", "good", "hat", "Common", 0, 0, 0, 0, 10)

    def equip_item(self, from_slot_index, to_slot_index):
        if self.scene.get_sprite_list("Slots")[from_slot_index].held_item is not None:
            if self.scene.get_sprite_list("Slots")[from_slot_index].held_item.name == self.scene.get_sprite_list("Slots")[to_slot_index].type_of_item:
                self.move_item(from_slot_index, to_slot_index)
            else:
                print("nope")
                print(self.scene.get_sprite_list("Slots")[from_slot_index].held_item.name)
                print(self.scene.get_sprite_list("Slots")[from_slot_index].held_item.item_rarity)
                print(self.scene.get_sprite_list("Slots")[to_slot_index].type_of_item)
                # ??????????????????????????????????????????????????? nwm o co chodzi pisze że twoże name = "hat a program pisze że name = "Common", a item_rarity = "hat", ale tak to działa(na testowniku działa), tylko ten błąd z tworzeniem te name
                # dodawania statystyk też nie zrobie, bo nwm jak dodać do playerObject w mainie byleco



    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw(pixelated=True)
        for s in self.scene.get_sprite_list("Slots"):
            s.show_item()
        self.scene.draw_hit_boxes((255, 0, 0), 1, ["Slots"])

    def on_update(self, delta_time):
        if arcade.key.I in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.I]
            self.gameView.camera.use()
            self.window.show_view(self.gameView)
        if arcade.key.X in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.X]
            self.move_item(0, 1)
        if arcade.key.D in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.D]
            self.delete_item(0)
        if arcade.key.A in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.A]
            self.add_item(3)
        if arcade.key.E in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.E]
            self.equip_item(0, 90)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)):
                    self.hold_item = s.held_item
                    self.hold_item_slot = s
                    self.hold_item_slot.can_show_item = False

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float,
                      _buttons: int, _modifiers: int):
        if self.hold_item:
            self.hold_item.position = x, y

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == 1:
            for s in self.scene.get_sprite_list("Slots"):
                if s.collides_with_point((x, y)) and s is not self.hold_item_slot and self.hold_item:
                    try:
                        s.held_item = self.hold_item
                        self.hold_item_slot.held_item = None
                        break
                    except:
                        self.hold_item_slot_last = self.hold_item


            if self.hold_item:
                self.hold_item = None
                self.hold_item_slot.can_show_item = True
                if self.hold_item_slot is not None:
                    self.hold_item_slot_last = self.hold_item_slot
                self.hold_item_slot = None

