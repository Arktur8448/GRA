# tu daj szarwiła
from pyglet import shapes


class Player:
    def __init__(self, x=0, y=0):
        self.playerSprite = None
        self.x = x
        self.y = y
        self.velocity_x, self.velocity_y = 100.0, 100.0
    def update_sprite(self):
        self.playerSprite.x = self.x
        self.playerSprite.y = self.y


def center_camera_to_player(window, player):
    window.view = window.view.translate((player.x, player.y))
