import arcade
import time
from pyglet.math import Vec2

DELTA_TIME = 1/60


class Player(arcade.Sprite):
    def __init__(self, sprite_path, x, y):
        super().__init__(filename=sprite_path, center_x=x, center_y=y, scale=1.6)
        self.movement_speed = 5000
        self.sprint_speed = 10000
        self.max_sprint_speed = 3600
        self.dodge_distance = 30 * self.movement_speed
        self.dodge_cooldown = 0.8
        self.doge_last_time = time.perf_counter() - self.dodge_cooldown
        self.keys = {}
        self.direction_move = "Down"
        self.can_move = True

        self.level = 1  # base staty
        self.exp = 0
        self.attribute_points = 0

        self.health = 25
        self.max_health = 30
        self.can_regen_health = True

        self.mana = 10
        self.max_mana = 30
        self.can_regen_mana = True

        self.stamina = 300
        self.max_stamina = 30
        self.can_regen_stamina = True

        self.strength = 10
        self.defence = 10
        self.agility = 10

        self.race = None
        self.weapon = None

    def movement(self, camera, camer_speed, width, height, physics_engine):
        """Pełny Ruch Gracza"""
        def check_move_key():  # aktualizacja pozycji w zależności od naciśniętych klawiszy
            if arcade.key.LSHIFT in self.keys and self.stamina > 0:
                self.can_regen_stamina = False
                speed = self.sprint_speed
                if arcade.key.W in self.keys or arcade.key.A in self.keys or arcade.key.S in self.keys or arcade.key.D in self.keys:
                    self.stamina -= 1/10
                    if self.stamina < 1:
                        self.stamina = -5  # jeśli zbyt mocno zużyjesz staminę to musisz bardziej odpocząć, przez chwilę ciężej ci złapać oddech
            else:
                speed = self.movement_speed
                self.can_regen_stamina = True

            if arcade.key.W in self.keys:
                physics_engine.apply_force(self, (0, speed))
                self.direction_move = "Up"
            elif arcade.key.S in self.keys:
                physics_engine.apply_force(self, (0, -speed))
                self.direction_move = "Down"
            else:
                self.change_y = 0

            if arcade.key.A in self.keys:
                physics_engine.apply_force(self, (-speed, 0))
                if arcade.key.W in self.keys:
                    self.direction_move = "UpLeft"
                elif arcade.key.S in self.keys:
                    self.direction_move = "DownLeft"
                else:
                    self.direction_move = "Left"
            elif arcade.key.D in self.keys:
                physics_engine.apply_force(self, (speed, 0))
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
                self.center_x - width / 2,
                self.center_y - height / 2
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

            physics_engine.apply_force(self, dash_force)

        if self.can_move:
            check_move_key()
            move_camera_to_player()

    def regenerate(self):
        if self.can_regen_health:
            self.health += DELTA_TIME / 5
        if self.can_regen_mana:
            self.mana += DELTA_TIME * 1
        if self.can_regen_stamina:
            if self.stamina < self.max_stamina / 2:
                self.stamina += DELTA_TIME * 3.5  # wolniejsze ładowanie staminy jeśli zużjesz ją w więcej niz w połowie
            elif self.stamina < self.max_stamina:
                self.stamina += DELTA_TIME * 3

        if self.health > self.max_health:
            self.health = self.max_health
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
