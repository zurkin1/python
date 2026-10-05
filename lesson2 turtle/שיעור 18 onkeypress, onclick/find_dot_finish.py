import random
import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgcolor('beige')

p = turtle.Turtle()
p.pu()
p.shape('blank')

def is_dot_on_screen():
    if abs(r_x) < win.window_width()/2 and abs(r_y) < win.window_height()/2:
        return True
    else:
        return False

def find_dot_func(x, y):
    p.goto(x, y)
    if p.distance((r_x, r_y)) < 100:
        win.setup(win.window_width() + 10, win.window_height() + 10)
    else:
        win.setup(win.window_width() - 10, win.window_height() - 10)

    # player won:
    if p.distance((r_x, r_y)) < 10:
        p.goto(0, 0)
        p.write("YOU WIN!", font=("arial", 28, "normal"))
    if is_dot_on_screen() == False:
        p.write("YOU LOSE!", font=("arial", 28, "normal"))




r_x = random.randint(-400, 400)
r_y = random.randint(-300, 300)

win.onclick(find_dot_func)
turtle.mainloop()