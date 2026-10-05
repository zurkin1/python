import turtle
win = turtle.Screen()
win.setup(600,600)
win.bgcolor('pink')

def check_location(x,y):
    if x>=0 and y>=0:
        print("RAVIA 1")
    if x >= 0 and y < 0:
        print("RAVIA 2")
    if x < 0 and y < 0:
        print("RAVIA 3")
    if x < 0 and y >= 0:
        print("RAVIA 4")

win.onclick(check_location)
turtle.mainloop()