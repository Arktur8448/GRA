import arcade
import player as pl
from pyglet.math import Vec2

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
SCREEN_TITLE = "GAME"
CAMERA_SPEED = 0.05 # szybokość z jaką kamera nadąża za graczem od 0 do 1


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.playerObject = None

        self.tile_map = None
        self.scene = None

        self.physics_engine = None

        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls")

        self.playerObject = pl.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.Sprite("Player.png"))  # tworzenie obietu gracza
        self.playerObject.update_pos()
        self.scene.add_sprite("Player", self.playerObject.playerSprite)

        self.scene.add_sprite("Walls", arcade.Sprite("Wall.png", center_x=SCREEN_WIDTH/2, center_y=SCREEN_HEIGHT/2 + 128))

        # Utworzenie silnkia fizyki nakładającego kolizje na Walls
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.playerObject.playerSprite, self.scene.get_sprite_list("Walls")
        )

        # Set up the player

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # Call draw() on all your sprite lists below
        self.scene.draw()

        self.camera.use()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        self.movement()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        self.playerObject.keys[key] = True

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        del self.playerObject.keys[key]

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    # Własne funkcje
    def movement(self):
        def check_move_key():  # aktualizacja pozycji w zależności od naciśniętych klawiszy
            if arcade.key.W in self.playerObject.keys:
                self.playerObject.playerSprite.change_y = self.playerObject.movement_speed
            elif arcade.key.S in self.playerObject.keys:
                self.playerObject.playerSprite.change_y = -self.playerObject.movement_speed
            else:
                self.playerObject.playerSprite.change_y = 0

            if arcade.key.A in self.playerObject.keys:
                self.playerObject.playerSprite.change_x = -self.playerObject.movement_speed
            elif arcade.key.D in self.playerObject.keys:
                self.playerObject.playerSprite.change_x = self.playerObject.movement_speed
            else:
                self.playerObject.playerSprite.change_x = 0

        def move_camera_to_player():
            position = Vec2(
                self.playerObject.playerSprite.center_x - self.width / 2,
                self.playerObject.playerSprite.center_y - self.height / 2
            )
            self.camera.move_to(position, CAMERA_SPEED)

        check_move_key()
        self.physics_engine.update()
        self.playerObject.update_pos()
        move_camera_to_player()


def main():
    """ Main function """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
