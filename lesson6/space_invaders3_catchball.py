import turtle
import os
import tkinter

# folder of the images, next to this file
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "res")

sc = turtle.Screen()
sc.bgcolor('cyan')
sc.setup(800,760)

class block():
    def __init__(self, start_x, start_y):
        self.player = turtle.Turtle()
        self.start_x = start_x
        self.player.pu()
        self.player.color('darkgreen')
        self.player.shape("square")
        self.player.shapesize(stretch_wid=1, stretch_len=4)
        self.player.setpos(start_x, start_y)
    def check_collide(self,ball):
        if  self.start_x < ball.xcor() < self.start_x + 80 and 310 > ball.ycor() > 290:
            return True
        return False
    def remove(self):
        self.player.hideturtle()
    def right(self):
        if self.player.xcor() < 320:
            self.player.setpos(self.player.xcor() + 10,self.player.ycor())
    def left(self):
        if self.player.xcor() > -320:
            self.player.setpos(self.player.xcor() - 10, self.player.ycor())

def pressRight():
    main_block.right()

def pressLeft():
    main_block.left()


block_list = []
for i in range(7):
    temp_block = block(i*100 - 300,300)
    block_list.append(temp_block)

#create the ball

ball = turtle.Turtle()
ball.pu()
# the picture is 500x500, subsample(25) shrinks it to 20x20
ball_image = tkinter.PhotoImage(file=os.path.join(RES, "bouncing_ball.png")).subsample(25)
sc.register_shape("ball", turtle.Shape("image", ball_image))
ball.shape("ball")
keep_playing = True
move_ver = 3
move_hor = 5

main_block = block(0,-300)
main_block.player.shapesize(1,8)

turtle.listen()
turtle.onkeypress(pressRight,"Right")
turtle.onkeypress(pressLeft,"Left")

while keep_playing:
    ball.setpos(ball.xcor() + move_hor,  ball.ycor() + move_ver)
    if ball.xcor() > 400 or ball.xcor() < -400:
        move_hor = move_hor * -1
    # going up

    for block in block_list:
        if block.check_collide(ball):
            print("collide")
            block.remove()
            block_list.remove(block)
            move_ver = move_ver*-1
    if ball.ycor() >= 380 or ball.ycor() <= -380:
        move_ver = move_ver * -1
    # check the bottom border
    if ball.ycor() <= -290 :
        if main_block.player.xcor() - 80 < ball.xcor() < main_block.player.xcor() + 80:
            move_ver = move_ver * -1
        else:
            keep_playing = False
            print("finished playing")



turtle.mainloop()