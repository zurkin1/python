import turtle
sc = turtle.Screen()
sc.setup(700,700)
sc.bgcolor('cyan')
shape_size = 1
ball = turtle.Turtle()
ball.shape('circle')
ball.pu()
ball.color('red')

player = turtle.Turtle()
player.shape('turtle')
player.color('maroon')
player.pu()
player.shapesize(shape_size)
keep_playing = True
move_ver = 3
move_hor = 5

def move_right():
    player.setheading(0)
    if player.xcor() < 350:
        player.setpos(player.xcor() + 5, player.ycor())

def move_left():
    player.setheading(180)
    if player.xcor() > -350:
        player.setpos(player.xcor() - 5, player.ycor())

def move_up():
    player.setheading(90)
    if player.ycor() < 350:
        player.setpos(player.xcor(), player.ycor() + 5)

def move_down():
    player.setheading(270)
    if player.ycor() > -350:
        player.setpos(player.xcor(), player.ycor() - 5)

turtle.onkey(move_right,'Right')
turtle.onkey(move_left,'Left')
turtle.onkey(move_up,'Up')
turtle.onkey(move_down,'Down')

turtle.listen()

while keep_playing:
    ball.setpos(ball.xcor() + move_hor,  ball.ycor() + move_ver)
    if ball.xcor() > 350 or ball.xcor() < -350:
        move_hor = move_hor * -1
    if ball.ycor() > 350 or ball.ycor() < -350:
        move_ver = move_ver * -1

turtle.mainloop()
