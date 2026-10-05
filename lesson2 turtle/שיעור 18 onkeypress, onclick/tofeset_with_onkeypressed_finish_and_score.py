import time
import turtle
sc = turtle.Screen()
sc.setup(700,700)
sc.bgcolor('cyan')
shape_size = 1
ball = turtle.Turtle()
ball.shape('circle')
ball.pu()
ball.color('red')
time=0
score=0
player = turtle.Turtle()
player.shape('turtle')
player.color('maroon')
player.pu()
player.shapesize(shape_size)
keep_playing = True
move_ver = 3
move_hor = 5

msg_player = turtle.Turtle()
msg_player.shape('blank')
msg_player.pu()
msg_player.goto(-80,200)
scr_player = turtle.Turtle()
scr_player.shape('blank')
scr_player.pu()
scr_player.goto(150,200)
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

turtle.onkeypress(move_right,'Right')
turtle.onkeypress(move_left,'Left')
turtle.onkeypress(move_up,'Up')
turtle.onkeypress(move_down,'Down')

turtle.listen()

while keep_playing:
    time = time + 1
    ball.setpos(ball.xcor() + move_hor,  ball.ycor() + move_ver)
    if ball.xcor() > 350 or ball.xcor() < -350:
        move_hor = move_hor * -1
    if ball.ycor() > 350 or ball.ycor() < -350:
        move_ver = move_ver * -1
    if time % 20 == 0:
        if player.distance(ball) < 40:
            msg_player.clear()
            scr_player.clear()
            score = score+1
            shape_size = shape_size + 0.3
            msg_player.write("Great Catch!", align="center", font=("Courier", 28, "bold"))
            scr_player.write("Score:"+ str(score), align="center", font=("Courier", 28, "bold"))
            player.shapesize(shape_size)

    if shape_size >= 10:
        keep_playing = False

turtle.mainloop()