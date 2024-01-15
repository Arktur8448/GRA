import arcade
import player as pl

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
SCREEN_TITLE = "GAME"
CAMERA_SPEED = 0.05  # szybokość z jaką kamera nadąża za graczem od 0 do 1


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color((231, 255, 80))

        self.playerObject = None

        self.tile_map = None
        self.scene = None

        self.physics_engine = None

        self.camera = None
        self.gui_camera = None

    def setup(self):
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.tile_map = arcade.load_tilemap("Maps/village/village.json", 2)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite_list("Player")
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.playerObject = pl.Player(735, 865, arcade.Sprite("Player.png", 0.75))  # tworzenie obietu gracza

        self.playerObject.update_pos()

        self.scene.add_sprite("Player", self.playerObject.playerSprite)

        # Utworzenie silnkia fizyki nakładającego kolizje na Walls
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=0)
        self.physics_engine.add_sprite(self.playerObject.playerSprite,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=1000000000000000000000000000000000000000,
                                       max_vertical_velocity=1000000000000000000000000000000000000000)
        self.physics_engine.add_sprite_list(self.scene.get_sprite_list("collision"),
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        self.scene.draw()

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
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.physics_engine.step()
        self.playerObject.movement(self.camera, CAMERA_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, self.physics_engine)

    def on_key_press(self, key, key_modifiers):
        self.playerObject.keys[key] = True

    def on_key_release(self, key, key_modifiers):
        del self.playerObject.keys[key]


def main():
    """ Main function """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
