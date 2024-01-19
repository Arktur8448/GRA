import arcade
import player as pl
import inventory

SCREEN_WIDTH = 992
SCREEN_HEIGHT = 572
SCREEN_TITLE = "THE GAME"
CAMERA_SPEED = 0.05  # szybokość z jaką kamera nadąża za graczem od 0 do 1


class GameWindow(arcade.Window):
    def __init__(self, width, height, title, player_object):
        super().__init__(width, height, title)
        self.playerObject = player_object

    def on_key_press(self, key, key_modifiers):
        self.playerObject.keys[key] = True

    def on_key_release(self, key, key_modifiers):
        try:
            del self.playerObject.keys[key]
        except:
            pass


class GameView(arcade.View):

    def __init__(self, player_object):
        super().__init__()

        arcade.set_background_color((231, 255, 80))

        self.playerObject = player_object

        self.tile_map = None
        self.scene = None

        self.physics_engine = None

        self.camera = None
        self.gui_camera = None

        self.inventoryView = None

    def setup(self):
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.tile_map = arcade.load_tilemap("Maps/village/village.json", 2)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.scene.add_sprite_list("Player")

        self.scene.add_sprite("Player", self.playerObject.playerSprite)

        # Utworzenie silnkia fizyki nakładającego kolizje na Walls
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=0)
        self.physics_engine.add_sprite(self.playerObject.playerSprite,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=1000000,
                                       max_vertical_velocity=1000000)
        self.physics_engine.add_sprite_list(self.scene.get_sprite_list("collision"),
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

        self.inventoryView = InventoryView(self.playerObject, self)

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        self.scene.draw(pixelated=True)
        self.scene.draw_hit_boxes((255, 0, 0), 1, ["Player", "collision"])

        self.camera.use()

        self.draw_gui()

    def draw_gui(self):
        self.gui_camera.use()
        hp = arcade.Text(
            f"HP: {int(self.playerObject.health)}/{self.playerObject.max_health}",
            10,
            SCREEN_HEIGHT - 30,
            arcade.color.BLACK,
            20,
            font_name="Kenney Blocks",
        )
        mana = arcade.Text(
            f"MANA: {int(self.playerObject.mana)}/{self.playerObject.max_mana}",
            10,
            SCREEN_HEIGHT - 60,
            arcade.color.BLACK,
            20,
            font_name="Kenney Blocks",
        )
        stamina = arcade.Text(
            f"STAMINA: {int(self.playerObject.stamina)}/{self.playerObject.max_stamina}",
            10,
            SCREEN_HEIGHT - 90,
            arcade.color.BLACK,
            20,
            font_name="Kenney Blocks",
        )
        box = arcade.draw_rectangle_filled(150, SCREEN_HEIGHT - 50, 300, 100, (205, 127, 50))
        hp.draw()
        mana.draw()
        stamina.draw()
        self.camera.use()

    def on_update(self, delta_time):
        self.physics_engine.step()
        self.playerObject.movement(self.camera, CAMERA_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, self.physics_engine)
        self.playerObject.regenerate()
        if arcade.key.I in self.playerObject.keys:
            self.window.show_view(self.inventoryView)
            del self.playerObject.keys[arcade.key.I]


class InventoryView(arcade.View):
    def __init__(self, player_object, game_view):
        super().__init__()
        self.playerObject = player_object
        self.gameView = game_view
        self.scene = None

        self.camera = None

        self.row_count = 10
        self.coulum_count = 9

        arcade.set_background_color((42, 42, 42))

    def on_show_view(self):
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Slots")
        for r in range(1, self.row_count+1):
            for c in range(1, self.coulum_count+1):
                self.scene.add_sprite("Slots", arcade.Sprite("sprites/inventory/Slot.png",
                                                             center_x=SCREEN_WIDTH/2+50*c, center_y=SCREEN_HEIGHT-25-50*r,
                                                             scale=1.5))

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw(pixelated=True)

    def on_update(self, delta_time):
        if arcade.key.I in self.playerObject.keys:
            self.gameView.camera.use()
            self.window.show_view(self.gameView)
            del self.playerObject.keys[arcade.key.I]


def main():
    player_object = pl.Player(735, 865, arcade.Sprite("sprites/player/player_start.png", 1.6))
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, player_object)
    start_view = GameView(player_object)
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
