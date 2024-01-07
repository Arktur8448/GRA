# tu daj szarwiła tą klase
class Player:
    def __init__(self, x=0, y=0):
        self.playerSprite = None
        self.x = x
        self.y = y
        self.velocity_x, self.velocity_y = 100.0, 100.0
    def update_sprite(self):
        self.playerSprite.x = self.x
        self.playerSprite.y = self.y


