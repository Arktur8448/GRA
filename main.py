import pyglet
from pyglet import shapes
from pyglet.window import key
from pyglet.gl import *
import player
import arcade


x_window = 960  # wymiary x okna
y_window = 540  # wymiary y okna
window = pyglet.window.Window(x_window, y_window, fullscreen=False)
batch = pyglet.graphics.Batch()  # do wyświetlania krztałtów

objects = []
tab = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
tab.reverse()  # inczej wysztko jest do góry nogami

dt = 1 / 60
playerObject = player.Player(x_window / 2, y_window / 2)
playerObject.playerSprite = shapes.Circle(x_window / 2, y_window / 2, 15, color=(168, 80, 100), batch=batch)


@window.event
def on_draw():  # Podstawowe Rysowanie Mapy
    window.clear()
    for r in range(len(tab)):  # r to ROW
        for i in range(len(tab[r])):  # i to ITEM
            if tab[r][i] == 1:
                objects.append(shapes.Rectangle(x=64 * i, y=64 * r,
                                                width=64, height=64,
                                                color=(111, 169, 117), batch=batch))
            elif tab[r][i] == 0:
                objects.append(shapes.Rectangle(x=64 * i, y=64 * r,
                                                width=64, height=64,
                                                color=(168, 160, 46), batch=batch))
    batch.draw() # rysowanie kwadratów kolizji

    image = pyglet.image.load('Map.png') # wycztanie mapy jako tekstury opengl
    texture = image.get_texture()
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    texture.width *= 2
    texture.height *= 2
    texture.blit(0, 0)

    playerObject.playerSprite.draw()

# sprawdzanie wciśnięcia klawiszy
@window.event
def on_key_release(symbol, modifiers):
    del playerObject.keys[symbol]


@window.event
def on_key_press( symbol, modifiers):
    playerObject.keys[symbol] = True


def move(dt):
    # x 300
    # y 600
    if key.W in playerObject.keys:
        playerObject.y += playerObject.velocity_y * dt
        playerObject.update_sprite()
        window.view = window.view.translate((0, -playerObject.velocity_y * dt, 0))
    if key.S in playerObject.keys:
        playerObject.y -= playerObject.velocity_y * dt
        playerObject.update_sprite()
        window.view = window.view.translate((0, playerObject.velocity_y * dt, 0))
    if key.A in playerObject.keys:
        playerObject.x -= playerObject.velocity_x * dt
        playerObject.update_sprite()
        window.view = window.view.translate((playerObject.velocity_x * dt, 0, 0))
    if key.D in playerObject.keys:
        playerObject.x += playerObject.velocity_x * dt
        playerObject.update_sprite()
        window.view = window.view.translate((-playerObject.velocity_x * dt, 0, 0))


pyglet.clock.schedule_interval(move, dt)
pyglet.app.run()
