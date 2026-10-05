
import random
import turtle


win = turtle.Screen()
win.setup(800,600)
win.bgcolor('beige')

p = turtle.Turtle()
p.pu()
p.shape('blank')

def find_dot_func(x, y):
    p.goto(x, y)
    if p.distance((r_x,r_y)) < 100:
        win.setup(win.window_width() + 10, win.window_height() + 10)
    else:
        win.setup(win.window_width() - 10, win.window_height() - 10)
    # player won:
    if p.distance((r_x,r_y)) < 10:
        p.goto(0,0)
        p.write("YOU WIN!", font = ("arial", 28, "normal"))
    #player lose the dot:
   

r_x = random.randint(-400,400)
r_y = random.randint(-300,300)

win.onclick(find_dot_func)
turtle.mainloop()
