import arcade
import player as pl
from pyglet.math import Vec2
import time

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

        self.dodge_cooldown = 0
        self.doge_last_time = 0

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls")

        self.playerObject = pl.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.Sprite("Player.png"))  # tworzenie obietu gracza
        self.playerObject.update_pos()
        self.dodge_cooldown = self.playerObject.dodge_cooldown
        self.doge_last_time = time.perf_counter() - self.playerObject.dodge_cooldown sss
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

    # Własne funkcje
    def movement(self):
        def check_move_key():  # aktualizacja pozycji w zależności od naciśniętych klawiszy
            if arcade.key.W in self.playerObject.keys:
                self.playerObject.playerSprite.change_y = self.playerObject.movement_speed
                self.playerObject.direction_move = "Up"
            elif arcade.key.S in self.playerObject.keys:
                self.playerObject.playerSprite.change_y = -self.playerObject.movement_speed
                self.playerObject.direction_move = "Down"
            else:
                self.playerObject.playerSprite.change_y = 0

            if arcade.key.A in self.playerObject.keys:
                self.playerObject.playerSprite.change_x = -self.playerObject.movement_speed
                if arcade.key.W in self.playerObject.keys:
                    self.playerObject.direction_move = "UpLeft"
                elif arcade.key.S in self.playerObject.keys:
                    self.playerObject.direction_move = "DownLeft"
                else:
                    self.playerObject.direction_move = "Left"
            elif arcade.key.D in self.playerObject.keys:
                self.playerObject.playerSprite.change_x = self.playerObject.movement_speed
                if arcade.key.W in self.playerObject.keys:
                    self.playerObject.direction_move = "UpRight"
                elif arcade.key.S in self.playerObject.keys:
                    self.playerObject.direction_move = "DownRight"
                else:
                    self.playerObject.direction_move = "Right"
            else:
                self.playerObject.playerSprite.change_x = 0

            if arcade.key.SPACE in self.playerObject.keys:
                if time.perf_counter() - self.doge_last_time > self.playerObject.dodge_cooldown:
                    dodge()

        def move_camera_to_player():
            position = Vec2(
                self.playerObject.playerSprite.center_x - self.width / 2,
                self.playerObject.playerSprite.center_y - self.height / 2
            )
            self.camera.move_to(position, CAMERA_SPEED)

        def dodge():
            self.doge_last_time = time.perf_counter()
            if self.playerObject.direction_move == "Left":
                self.playerObject.playerSprite.change_x = -self.playerObject.movement_speed * self.playerObject.dodge_distance
            elif self.playerObject.direction_move == "UpLeft":
                self.playerObject.playerSprite.change_y = self.playerObject.movement_speed * self.playerObject.dodge_distance
                self.playerObject.playerSprite.change_x = -self.playerObject.movement_speed * self.playerObject.dodge_distance
            elif self.playerObject.direction_move == "Up":
                self.playerObject.playerSprite.change_y = self.playerObject.movement_speed * self.playerObject.dodge_distance

            elif self.playerObject.direction_move == "UpRight":
                self.playerObject.playerSprite.change_y = self.playerObject.movement_speed * self.playerObject.dodge_distance
                self.playerObject.playerSprite.change_x = self.playerObject.movement_speed * self.playerObject.dodge_distance

            elif self.playerObject.direction_move == "Right":
                self.playerObject.playerSprite.change_x = self.playerObject.movement_speed * self.playerObject.dodge_distance

            elif self.playerObject.direction_move == "DownRight":
                self.playerObject.playerSprite.change_y = -self.playerObject.movement_speed * self.playerObject.dodge_distance
                self.playerObject.playerSprite.change_x = self.playerObject.movement_speed * self.playerObject.dodge_distance

            elif self.playerObject.direction_move == "Down":
                self.playerObject.playerSprite.change_y = -self.playerObject.movement_speed * self.playerObject.dodge_distance
                
            elif self.playerObject.direction_move == "DownLeft":
                self.playerObject.playerSprite.change_y = -self.playerObject.movement_speed * self.playerObject.dodge_distance
                self.playerObject.playerSprite.change_x = -self.playerObject.movement_speed * self.playerObject.dodge_distance

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
