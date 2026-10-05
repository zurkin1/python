import turtle
player = turtle.Turtle()
player.shape('turtle')
player.color('purple')


def move_right():
    player.setheading(0)
    player.forward(10)


def move_left():
    player.setheading(180)
    player.forward(10)


def move_up():
    player.setheading(90)
    player.forward(10)


def move_down():
    player.setheading(270)
    player.forward(10)



turtle.listen()
turtle.onkey(move_right,'Right')
turtle.onkey(move_left,'Left')
turtle.onkey(move_up,'Up')
turtle.onkey(move_down,'Down')

turtle.mainloop()