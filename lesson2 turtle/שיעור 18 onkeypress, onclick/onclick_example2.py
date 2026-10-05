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


def move_turtle(x,y):
    #move_x  = random.randint(-300,300)
    #move_y = random.randint(-300, 300)
    onclick_player.goto(x, y)
    onclick_player.write((x,y))


win.onclick(move_turtle)
turtle.mainloop()