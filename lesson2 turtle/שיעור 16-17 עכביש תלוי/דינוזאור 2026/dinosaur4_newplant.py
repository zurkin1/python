import turtle
import random

sc = turtle.Screen()
sc.bgcolor('beige')
sc.setup(1000,900)


sc.register_shape('dino.gif')
sc.register_shape('dino1.gif')
sc.register_shape('dino2.gif')
sc.register_shape('plant.gif')

dino = turtle.Turtle()
dino_image = 'dino.gif'
dino.pu()
dino.shape(dino_image)
dino.goto(-400,-350)

plant = turtle.Turtle()
plant_image = 'plant.gif'
plant.shape(plant_image)
plant.pu()
plant.goto(450,-350)
continue_playing = True
score = 0

def jump():
    for i in range(20):
        dino.setpos(dino.xcor(), dino.ycor()+10)
        plant.back(10)
    for i in range(20):
        dino.setpos(dino.xcor(), dino.ycor()-10)
        plant.back(10)


turtle.listen()
turtle.onkey(jump,'Up')
while continue_playing:
    score = score + 1
    if plant.xcor() < -550:
        plant.speed(10)
        plant.hideturtle()
        plant.setpos(500,-350)
        plant.showturtle()
        plant.speed(2)
    else:
        plant.back(10)
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
