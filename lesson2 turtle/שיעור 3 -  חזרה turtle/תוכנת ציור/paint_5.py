import turtle
from contextlib import closing

wn = turtle.Screen()
wn.bgcolor('cyan')
colors=['yellow','blue','red','green']
locations=[(-140,100),(100,100),(-140,-80),(100,-80)]
i = 0
draw_color=""
draw_line = 0

def set_pu():
    player2.pu()

def set_pd():
    print("pd")
    player2.pd()

def start_drawing(x,y):
    player2.goto(x,y)

def set_properties(x,y):
    global draw_color
    global draw_line
    if draw_color != "" and draw_line != 0:
        player2.color(draw_color)
        player2.pensize(draw_line)
        start_drawing(x,y)
    if ( x>-200 and x<0 and y>-200 and y<0):
        if draw_color == "":
            draw_color="blue"
        elif draw_line==0:
            draw_line = 1
    if ( x>-200 and x<0 and y>0 and y<200):
        if draw_color == "":
            draw_color = "red"
        elif draw_line == 0:
            draw_line = 2
    if ( x>0 and x<200 and y>-200 and y<0):
        if draw_color == "":
            draw_color = "yellow"
        elif draw_line == 0:
            draw_line = 3
    if ( x>0 and x<200 and y>0 and y<200):
        if draw_color == "":
            draw_color = "green"
        elif draw_line == 0:
            draw_line = 4
    if draw_color != "" and draw_line != 0:
        player.clear()
    print(x,y)


def draw_window(player):
    for i in range(4):
        player.fillcolor(colors[i])
        player.begin_fill()
        for i in range(4):
            player.forward(200)
            player.rt(90)
        player.rt(90)
        player.end_fill()

def draw_lines():
    pen_size=1
    player.shape('blank')
    for location in locations:
        player.pu()
        player.pensize(pen_size)
        player.goto(location)
        player.pd()
        player.setheading(45)
        player.forward(40)
        pen_size = pen_size + 1


player = turtle.Turtle()
player2 = turtle.Turtle()
player.pensize(4)
player.color('navy')
#player.shape('blank')
draw_window(player)
draw_lines()
player.pu()
player.goto(-200,250)
player.write('1.choose color')
player.goto(-200,220)
player.write('2.choose pensize')

wn.listen()
wn.onclick(set_properties)
wn.onkeypress(set_pu,"u")
wn.onkeypress(set_pd,"d")
turtle.mainloop()