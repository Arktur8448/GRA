import arcade
import time

SLASH_COOLDOWN = 0.5
MOUSE_MARGIN = 40
SCREEN_WIDTH = 992
SCREEN_HEIGHT = 572


class Slash(arcade.Sprite):
    def __init__(self,center_x, center_y, image_width=55, image_height=65, scale=1):
        super().__init__(filename="sprites/player/slash.png",
                         center_x=center_x, center_y=center_y,
                         image_width=image_width, image_height=image_height, scale=scale)
        self.direction = None


def get_slash(player_object, scene, x, y):
    if len(scene.get_sprite_list("Slash")) == 0:
        slash = Slash(center_x=player_object.x, center_y=player_object.y)
        x -= SCREEN_WIDTH / 2
        y -= SCREEN_HEIGHT / 2
        if -MOUSE_MARGIN < x < MOUSE_MARGIN:
            if y > 0:
                slash.direction = "Up"
                slash.center_x += 0
                slash.center_y += 60
            else:
                slash.direction = "Down"
                slash.turn_right(180)
                slash.center_x += 0
                slash.center_y += -55
        elif -MOUSE_MARGIN < y < MOUSE_MARGIN:
            if x > 0:
                slash.direction = "Right"
                slash.turn_right(90)
                slash.center_x += 50
                slash.center_y += 0
            else:
                slash.direction = "Left"
                slash.turn_left(90)
                slash.center_x += -50
                slash.center_y += 0
        else:
            if x > MOUSE_MARGIN and y > MOUSE_MARGIN:
                slash.direction = "UpRight"
                slash.turn_right(45)
                slash.center_x += 25
                slash.center_y += 50
            elif x < MOUSE_MARGIN < y:
                slash.direction = "UpLeft"
                slash.turn_left(45)
                slash.center_x += -25
                slash.center_y += 50
            elif x > MOUSE_MARGIN > y:
                slash.direction = "DownRight"
                slash.turn_right(135)
                slash.center_x += 25
                slash.center_y += -50
            elif x < MOUSE_MARGIN and y < MOUSE_MARGIN:
                slash.direction = "DownLeft"
                slash.turn_left(135)
                slash.center_x += -25
                slash.center_y += -50

        print(slash.direction)
        scene.add_sprite("Slash", slash)


time_slash = time.perf_counter() - SLASH_COOLDOWN


def update(player_object, scene):
    global time_slash
    if len(scene.get_sprite_list("Slash")) > 0:
        if time.perf_counter() - time_slash >= SLASH_COOLDOWN:
            for s in scene.get_sprite_list("Slash"):
                s.kill()
        else:
            for slash in scene.get_sprite_list("Slash"):
                slash.center_x = player_object.x
                slash.center_y = player_object.y
                match slash.direction:
                    case "Down":
                        slash.center_x += 0
                        slash.center_y += -55
                    case "DownLeft":
                        slash.center_x += -25
                        slash.center_y += -50
                    case "Left":
                        slash.center_x += -50
                        slash.center_y += 0
                    case "UpLeft":
                        slash.center_x += -25
                        slash.center_y += 50
                    case "Up":
                        slash.center_x += 0
                        slash.center_y += 60
                    case "UpRight":
                        slash.center_x += 25
                        slash.center_y += 50
                    case "Right":
                        slash.center_x += 50
                        slash.center_y += 0
                    case "DownRight":
                        slash.center_x += 25
                        slash.center_y += -50
    else:
        time_slash = time.perf_counter()
