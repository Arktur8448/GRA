import arcade
import time
from pyglet.math import Vec2


class Player:
    def __init__(self, x=0, y=0, sprite=None):
        self.playerSprite = sprite
        self.movement_speed = 5000
        self.sprint_speed = 10000
        self.max_sprint_speed = 3600
        self.dodge_distance = 30 * self.movement_speed
        self.dodge_cooldown = 0.8
        self.doge_last_time = time.perf_counter() - self.dodge_cooldown
        self.x = x
        self.y = y
        self.playerSprite.center_x = self.x
        self.playerSprite.center_y = self.y
        self.keys = {}
        self.direction_move = "Down"

        self.level = 1  # base staty
        self.exp = 0
        self.attribute_points = 0
        self.health = 25
        self.max_health = 30
        self.mana = 10
        self.max_mana = 30
        self.stamina = 20
        self.max_stamina = 30
        self.strength = 10
        self.defence = 10
        self.agility = 10
        self.race = None
        self.weapon = None

    def update_pos(self):
        """Update Pozycji Gracza"""
        self.x = self.playerSprite.center_x
        self.y = self.playerSprite.center_y

    def movement(self, camera, camer_speed, width, height, physics_engine):
        """Pełny Ruch Gracza"""
        def check_move_key():  # aktualizacja pozycji w zależności od naciśniętych klawiszy
            if arcade.key.LSHIFT in self.keys and self.stamina > 0:
                speed = self.sprint_speed
                if arcade.key.W in self.keys or arcade.key.A in self.keys or arcade.key.S in self.keys or arcade.key.D in self.keys:
                    self.stamina -= 1/10
                    if self.stamina < 1:
                        self.stamina = -5  # jeśli zbyt mocno zużyjesz staminę to musisz bardziej odpocząć, przez chwilę ciężej ci złapać oddech
            else:
                speed = self.movement_speed
                if self.stamina < self.max_stamina / 2:
                    self.stamina += 1/25  # wolniejsze łądowanie staminy jeśli zużjesz ją w więcej niz w połowie
                elif self.stamina < self.max_stamina:
                    self.stamina += 1/20

            if arcade.key.W in self.keys:
                physics_engine.apply_force(self.playerSprite, (0, speed))
                self.direction_move = "Up"
            elif arcade.key.S in self.keys:
                physics_engine.apply_force(self.playerSprite, (0, -speed))
                self.direction_move = "Down"
            else:
                self.playerSprite.change_y = 0

            if arcade.key.A in self.keys:
                physics_engine.apply_force(self.playerSprite, (-speed, 0))
                if arcade.key.W in self.keys:
                    self.direction_move = "UpLeft"
                elif arcade.key.S in self.keys:
                    self.direction_move = "DownLeft"
                else:
                    self.direction_move = "Left"
            elif arcade.key.D in self.keys:
                physics_engine.apply_force(self.playerSprite, (speed, 0))
                if arcade.key.W in self.keys:
                    self.direction_move = "UpRight"
                elif arcade.key.S in self.keys:
                    self.direction_move = "DownRight"
                else:
                    self.direction_move = "Right"

            if arcade.key.SPACE in self.keys:
                if time.perf_counter() - self.doge_last_time > self.dodge_cooldown and self.stamina > 10:
                    self.stamina -= 10
                    dodge()

        def move_camera_to_player():
            position = Vec2(
                self.playerSprite.center_x - width / 2,
                self.playerSprite.center_y - height / 2
            )
            camera.move_to(position, camer_speed)

        def dodge():
            self.doge_last_time = time.perf_counter()
            dash_force = (0, 0)
            if self.direction_move == "Left":
                dash_force = (-self.dodge_distance, 0)
            elif self.direction_move == "UpLeft":
                dash_force = (-self.dodge_distance, self.dodge_distance)
            elif self.direction_move == "Up":
                dash_force = (0, self.dodge_distance)

            elif self.direction_move == "UpRight":
                dash_force = (self.dodge_distance, self.dodge_distance)

            elif self.direction_move == "Right":
                dash_force = (self.dodge_distance, 0)

            elif self.direction_move == "DownRight":
                dash_force = (self.dodge_distance, -self.dodge_distance)

            elif self.direction_move == "Down":
                dash_force = (0, -self.dodge_distance)

            elif self.direction_move == "DownLeft":
                dash_force = (-self.dodge_distance, -self.dodge_distance)

            physics_engine.apply_force(self.playerSprite, dash_force)

        check_move_key()
        self.update_pos()
        move_camera_to_player()

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def level_up(self):
        if self.exp >= self.level*50:
            self.level += 1
            self.attribute_points += 1
            return True
        else:
            return self.level*50-self.exp

    def redistribute_points(self, stat):
        if stat == "1":
            self.health += 10
            return True
        elif stat == "2":
            self.mana += 10
            return True
        elif stat == "3":
            self.strength += 5
            return True
        elif stat == "4":
            self.defence += 5
            return True
        elif stat == "5":
            self.agility += 5
            return True
        else:
            return False
