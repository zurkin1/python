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
player.shapesize(shape_size)
keep_playing = True
move_ver = 3
move_hor = 5

while keep_playing:
    ball.setpos(ball.xcor() + move_hor,  ball.ycor() + move_ver)
    if ball.xcor() > 350 or ball.xcor() < -350:
        move_hor = move_hor * -1
    if ball.ycor() > 350 or ball.ycor() < -350:
        move_ver = move_ver * -1


turtle.mainloop()