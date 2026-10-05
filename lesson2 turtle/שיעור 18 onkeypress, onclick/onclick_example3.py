import random
import turtle
win = turtle.Screen()
win.setup(600,600)
win.bgcolor('pink')
player = turtle.Turtle()
player.pu()
player.shape('blank')

onclick_player = turtle.Turtle()
onclick_player.color('dark red')

onclick_player.shape('turtle')

def press_turtle(x,y):
   size  = random.randint(1,4)
   onclick_player.shapesize(size)

def move_turtle(x,y):
    #move_x  = random.randint(-300,300)
    #move_y = random.randint(-300, 300)
    onclick_player.goto(x, y)
    onclick_player.write((x,y))


win.onclick(move_turtle)
onclick_player.onclick(press_turtle)
turtle.mainloop()