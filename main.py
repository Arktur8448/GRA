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

        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        self.tile_map = arcade.load_tilemap("Maps/village/village.json", 2)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite_list("Player")
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.playerObject = pl.Player(735, 865, arcade.Sprite("Player.png", 0.75))  # tworzenie obietu gracza

        self.playerObject.update_pos()

        self.scene.add_sprite("Player", self.playerObject.playerSprite)

        # Utworzenie silnkia fizyki nakładającego kolizje na Walls
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.playerObject.playerSprite, self.scene.get_sprite_list("collision")
        )

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        self.scene.draw()

        self.camera.use()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
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
