import arcade
import time

SLASH_COOLDOWN = 0.5


class Slash(arcade.Sprite):
    def __init__(self,center_x, center_y, image_width=60, image_height=20, scale=2):
        super().__init__(filename="sprites/player/Player.png",
                         center_x=center_x, center_y=center_y,
                         image_width=image_width, image_height=image_height, scale=scale)
        self.direction = None


def get_slash(player_object, scene):
    if len(scene.get_sprite_list("Slash")) == 0:
        slash = Slash(center_x=player_object.x, center_y=player_object.y)
        match player_object.direction_move:
            case "Down":
                slash.turn_right(180)
                slash.center_x += 0
                slash.center_y += -50
                slash.direction = player_object.direction_move
            case "DownLeft":
                slash.turn_left(135)
                slash.center_x += -25
                slash.center_y += -50
                slash.direction = player_object.direction_move
            case "Left":
                slash.turn_left(90)
                slash.center_x += -50
                slash.center_y += 0
                slash.direction = player_object.direction_move
            case "UpLeft":
                slash.turn_left(45)
                slash.center_x += -25
                slash.center_y += 50
                slash.direction = player_object.direction_move
            case "Up":
                slash.center_x += 0
                slash.center_y += 50
                slash.direction = player_object.direction_move
            case "UpRight":
                slash.turn_right(45)
                slash.center_x += 25
                slash.center_y += 50
                slash.direction = player_object.direction_move
            case "Right":
                slash.turn_right(90)
                slash.center_x += 50
                slash.center_y += 0
                slash.direction = player_object.direction_move
            case "DownRight":
                slash.turn_right(135)
                slash.center_x += 25
                slash.center_y += -50
                slash.direction = player_object.direction_move

        scene.add_sprite("Slash", slash)


time_slash = time.perf_counter() - SLASH_COOLDOWN


def update(player_object, scene):
    global time_slash
    if len(scene.get_sprite_list("Slash")) > 0:
        print(time.perf_counter() - time_slash)
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
                        slash.center_y += -50
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
                        slash.center_y += 50
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
