import turtle
wn = turtle.Screen()
wn.title("pong by Ana")
wn.bgcolor('pink')
wn.setup(800,600)
#wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 5
ball.dy = 5
score = 0
run = True

def puddle_a_up():
    y=paddle_a.ycor()
    y = y+20
    if y < 280:
        paddle_a.sety(y)
def puddle_a_down():
    y=paddle_a.ycor()
    y = y-20
    if y > -280:
        paddle_a.sety(y)
def puddle_b_up():
    y=paddle_b.ycor()
    y = y+20
    if y < 280:
        paddle_b.sety(y)
def puddle_b_down():
    y=paddle_b.ycor()
    y = y-20
    if y > -280:
        paddle_b.sety(y)
def exit_game():
    turtle.done()

wn.listen()
wn.onkeypress(puddle_b_up,"Up")
wn.onkeypress(puddle_b_down,"Down")
wn.onkeypress(puddle_a_up,"Right")
wn.onkeypress(puddle_a_down,"Left")


while True:

    score  = score +1
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if (ball.ycor()> 290):
        ball.sety(290)
        ball.dy  = ball.dy*-1

    if (ball.ycor()< -290):
        ball.sety(-290)
        ball.dy  = ball.dy*-1

    if (ball.xcor()> 390):
        ball.setx(390)
        ball.dx  = ball.dx*-1

    if (ball.xcor()< -390):
        ball.setx(-390)
        ball.dx  = ball.dx * -1

    #collition
    if ball.xcor() > 350:
        if paddle_b.ycor()+50 > ball.ycor() > paddle_b.ycor()-50:
            ball.dx = ball.dx * -1
        else:
            exit_game()
           # turtle.done()

    turtle.update()
            #turtle.done()
