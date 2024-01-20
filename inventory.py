import arcade
import items

SCREEN_WIDTH = 992
SCREEN_HEIGHT = 572


class Slot(arcade.Sprite):  # Slot jest jednocześnie spritem i obiektem z funckjami i wartościami
    def __init__(self, slot_sprite, center_x, center_y, scale, held_item=None):
        super().__init__(slot_sprite, center_x=center_x, center_y=center_y, scale=scale)
        self.held_item = held_item


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

        self.scene.get_sprite_list("Slots")[0].held_item = items.Item("TEST", "Tesotwnik", 20, 10)  # pokaz jak działają itemy cz1
        # wszystkie sloty są przechowywane przez sprite_list Slots. Tą spritelist przechowuje scena. Spitelist przechowuje sloty jako tablice.

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw(pixelated=True)

    def on_update(self, delta_time):
        if arcade.key.I in self.playerObject.keys:
            self.gameView.camera.use()
            self.window.show_view(self.gameView)
            del self.playerObject.keys[arcade.key.I]
        if arcade.key.X in self.playerObject.keys:  # pokaz jak działają itemy cz2
            print(self.scene.get_sprite_list("Slots")[0].held_item)  # wyświtlenie testowego itemu

