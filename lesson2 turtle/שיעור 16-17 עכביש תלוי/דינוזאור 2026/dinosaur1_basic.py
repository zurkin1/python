import turtle
import random

sc = turtle.Screen()
sc.bgcolor('beige')
sc.setup(1000, 900)

sc.register_shape('dino.gif')
sc.register_shape('dino1.gif')
sc.register_shape('dino2.gif')


dino = turtle.Turtle()
dino_image = 'dino.gif'
dino.pu()
dino.shape(dino_image)
dino.goto(-400, -350)

continue_playing = True
score = 0


while continue_playing:
    score = score + 1
    if dino_image == 'dino.gif':
        dino_image = 'dino1.gif'
        dino.shape(dino_image)
    if dino_image == 'dino1.gif':
        dino_image = 'dino2.gif'
        dino.shape(dino_image)
    if dino_image == 'dino2.gif':
        dino_image = 'dino.gif'
        dino.shape(dino_image)

turtle.mainloop()
