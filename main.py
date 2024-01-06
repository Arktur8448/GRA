import pyglet
from pyglet import shapes

x_window = 1920  # wymiary x okna
y_window = 1080  # wymiary y okna
window = pyglet.window.Window(x_window, y_window, fullscreen=True)
batch = pyglet.graphics.Batch()  # do wyświetlania krztałtów

objects = []
tab = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]
tab.reverse()  # inczej wysztko jest do góry nogami


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
    player = shapes.Circle(x_window / 2, y_window / 2, 50, color=(168, 80, 100), batch=batch)  # testowy gracz
    batch.draw()


pyglet.app.run()
