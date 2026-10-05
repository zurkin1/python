import turtle
import math

player1 = turtle.Turtle()
player1.shape('turtle')
player1.color('green')
player1.shapesize(4)
player1.pu()
player1.goto(-300,300)

player2 = turtle.Turtle()
player2.shape('turtle')
player2.color('blue')
player2.shapesize(4)
player2.pu()
player2.goto(-300,-300)

pizza = turtle.Turtle()
pizza.shape('triangle')
pizza.color('yellow')
pizza.shapesize(3)
continue_playing = True
current_player = player1

while continue_playing:

    angle = turtle.numinput(current_player.color(), 'enter angle')
    steps = turtle.numinput(current_player.color(), 'enter steps')

    if current_player.ycor() > pizza.ycor():
        current_player.right(angle)
    else:
        current_player.left(angle)
    current_player.forward(steps)

    if pizza.distance(current_player)>10:
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    else:
        continue_playing = False


turtle.mainloop()