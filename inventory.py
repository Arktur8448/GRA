import arcade
import items

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

    def show_item(self):
        if self.held_item is not None:
            sprite = arcade.Sprite("sprites/player/Player.png",
                                   center_x=self.center_x, center_y=self.center_y,
                                   scale=0.3)
            sprite.draw()


class InventoryView(arcade.View):
    def __init__(self, player_object, game_view):
        super().__init__()
        self.playerObject = player_object
        self.gameView = game_view
        self.scene = None

        self.camera = None

        self.row_count = 10
        self.coulum_count = 9

    def on_show_view(self):
        arcade.set_background_color((42, 42, 42))
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Slots")
        for r in range(1, self.row_count + 1):
            for c in range(1, self.coulum_count + 1):
                self.scene.add_sprite("Slots", Slot("sprites/inventory/Slot.png",
                                                    center_x=SCREEN_WIDTH / 2 + 50 * c,
                                                    center_y=SCREEN_HEIGHT - 25 - 50 * r,
                                                    scale=1.5))

        self.scene.add_sprite("Slots", Slot("sprites/player/player_base.png",
                                            center_x=250,
                                            center_y=SCREEN_HEIGHT / 1.5,
                                            scale=5))
        self.scene.add_sprite("Slots", Slot("sprites/inventory/hat.png",
                                            center_x=249,
                                            center_y=SCREEN_HEIGHT - 60,
                                            scale=1.5))
        x = 150
        for i in range(0, 2):
            self.scene.add_sprite("Slots", Slot("sprites/inventory/ring.png",
                                                center_x=x,
                                                center_y=SCREEN_HEIGHT - 132,
                                                scale=1))
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

        self.scene.get_sprite_list("Slots")[0].held_item = 1

    def move_item(self, form_slot_index, to_slot_index):
        tmp = self.scene.get_sprite_list("Slots")[to_slot_index].held_item
        self.scene.get_sprite_list("Slots")[to_slot_index].held_item = self.scene.get_sprite_list("Slots")[form_slot_index].held_item
        self.scene.get_sprite_list("Slots")[form_slot_index].held_item = tmp

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
        if arcade.key.X in self.playerObject.keys:
            del self.playerObject.keys[arcade.key.X]
            self.move_item(0, 1)
