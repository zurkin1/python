import turtle
sc = turtle.Screen()
sc.setup(700,700)
sc.bgcolor('cyan')

ball = turtle.Turtle()
ball.shape('circle')
keep_playing = True
move_ver = 3
move_hor = 5

while keep_playing:
    ball.setpos(ball.xcor() + move_hor,  ball.ycor() + move_ver)
    if ball.xcor() > 350 or ball.xcor() < -350:
        print(ball.xcor())
        move_hor = move_hor * -1
    if ball.ycor() > 350 or ball.ycor() < -350:
        move_ver = move_ver * -1
        print(ball.ycor())

turtle.mainloop()