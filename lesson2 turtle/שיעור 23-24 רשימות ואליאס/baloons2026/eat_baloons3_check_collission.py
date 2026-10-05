
import random
import time
import turtle
bird = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('beige')
wn.setup(800,600)
wn.addshape('bird.gif')
bird.shape('bird.gif')
bird.pu()
score = 0

baloon_image_list = ['red.gif','pink.gif','green.gif','yellow.gif']
for img in baloon_image_list:
    wn.addshape(img)
baloons_on_screen = []

def move_right():
    if bird.xcor() < 400:
        bird.goto(bird.xcor()+20,bird.ycor())

def move_left():
    if bird.xcor() > -400:
        bird.goto(bird.xcor()-20,bird.ycor())

def move_up():
    if bird.xcor() < 400:
        bird.goto(bird.xcor(),bird.ycor()+20)

def move_down():
    if bird.xcor() > -400:
        bird.goto(bird.xcor(),bird.ycor()-20)

def check_collission():
    global score
    for ballon in baloons_on_screen:
        if ballon.distance(bird.xcor()+50,bird.ycor()) < 35:
            score = score + 1
            ballon.hideturtle()
            baloons_on_screen.remove(ballon)
def finish_game():
    print(score)
wn.listen()
wn.onkeypress(move_up,'Up')
wn.onkeypress(move_down,'Down')
wn.onkeypress(move_right,'Right')
wn.onkeypress(move_left,'Left')

while len(baloons_on_screen) < 10:
    t = turtle.Turtle()
    t.speed(1)
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    rand_image = random.choice(baloon_image_list)
    t.pu()
    t.shape('blank')
    t.goto(x,y)
    t.shape(rand_image)
    baloons_on_screen.append(t)
    check_collission()
finish_game()
wn.mainloop()