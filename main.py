import pyglet
from pyglet import shapes
from pyglet.window import key
import player

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
playerObject.playerSprite = shapes.Circle(x_window / 2, y_window / 2, 25, color=(168, 80, 100), batch=batch)
w, a, s, d = False, False, False, False


@window.event
def on_draw():  # Podstawowe Rysowanie Mapy
    window.clear()
    for r in range(len(tab)):  # r to ROW
        for i in range(len(tab[r])):  # i to ITEM
            if tab[r][i] == 1:
                objects.append(shapes.Rectangle(x=x_window / len(tab[r]) * i, y=y_window / len(tab) * r,
                                                width=x_window / len(tab[r]), height=y_window / len(tab),
                                                color=(111, 169, 117), batch=batch))
            elif tab[r][i] == 0:
                objects.append(shapes.Rectangle(x=x_window / len(tab[r]) * i, y=y_window / len(tab) * r,
                                                width=x_window / len(tab[r]), height=y_window / len(tab),
                                                color=(168, 160, 46), batch=batch))
    batch.draw()
    playerObject.playerSprite.draw()


@window.event
def on_key_press(symbol, modifiers):
    global w, a, s, d
    if symbol == key.W:
        w = True
    elif symbol == key.A:
        a = True
    elif symbol == key.S:
        s = True
    elif symbol == key.D:
        d = True


@window.event
def on_key_release(symbol, modifiers):
    global w, a, s, d
    if symbol == key.W:
        w = False
    elif symbol == key.A:
        a = False
    elif symbol == key.S:
        s = False
    elif symbol == key.D:
        d = False


def update(dt):
    if w:
        playerObject.y += playerObject.velocity_y * dt
        playerObject.update_sprite()
        window.view = window.view.translate((0, -playerObject.velocity_y * dt, 0))
    if s:
        playerObject.y -= playerObject.velocity_y * dt
        playerObject.update_sprite()
        window.view = window.view.translate((0, playerObject.velocity_y * dt, 0))
    if a:
        playerObject.x -= playerObject.velocity_x * dt
        playerObject.update_sprite()
        window.view = window.view.translate((playerObject.velocity_x * dt, 0, 0))
    if d:
        playerObject.x += playerObject.velocity_x * dt
        playerObject.update_sprite()
        window.view = window.view.translate((-playerObject.velocity_x * dt, 0, 0))


pyglet.clock.schedule_interval(update, dt)
pyglet.app.run()
