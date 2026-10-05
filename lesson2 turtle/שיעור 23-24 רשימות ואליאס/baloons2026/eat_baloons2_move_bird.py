
import random
import turtle
bird = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('beige')
wn.setup(800,600)
wn.addshape('bird.gif')
bird.shape('bird.gif')
bird.pu()

baloon_image_list = ['red.gif','pink.gif','green.gif','yellow.gif']
for img in baloon_image_list:
    wn.addshape(img)
baloons_on_screen = []

def move_right():
    if bird.xcor() < 400:
        bird.goto(bird.xcor()+10,bird.ycor())

def move_left():
    if bird.xcor() > -400:
        bird.goto(bird.xcor()-10,bird.ycor())

def move_up():
    if bird.xcor() < 400:
        bird.goto(bird.xcor(),bird.ycor()+10)

def move_down():
    if bird.xcor() > -400:
        bird.goto(bird.xcor(),bird.ycor()-10)

wn.listen()
turtle.onkeypress(move_up,'Up')
turtle.onkeypress(move_down,'Down')
wn.onkeypress(move_right,'Right')
turtle.onkeypress(move_left,'Left')
while True:
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    rand_image = random.choice(baloon_image_list)
    t = turtle.Turtle()
    t.pu()
    t.shape('blank')
    t.goto(x,y)
    t.shape(rand_image)
    baloons_on_screen.append(t)
wn.mainloop()