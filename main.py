import pyglet
import  time
import random
window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    print(f'The window was resized to {width},{height}')
image = pyglet.resource.image('kitten.png')
@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
@window.event
def on_key_press(symbol, modifiers):
    window.set_location(random.randint(0,1900), random.randint(0,1000))

pyglet.app.run()