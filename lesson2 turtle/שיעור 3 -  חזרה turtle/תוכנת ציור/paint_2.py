import turtle
from contextlib import closing

wn = turtle.Screen()
wn.bgcolor('cyan')

def set_properties(x,y):
    global draw_color
    if ( x>-200 and x<0 and y>-200 and y<0):
        draw_color="blue"
    if ( x>-200 and x<0 and y>0 and y<200):
        draw_color="red"
    if ( x>0 and x<200 and y>-200 and y<0):
        draw_color="yellow"
    if ( x>0 and x<200 and y>0 and y<200):
        draw_color="green"
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



colors=['yellow','blue','red','green']
i = 0
draw_color=""
player = turtle.Turtle()
player.pensize(4)
player.color('navy')
#player.shape('blank')
draw_window(player)


wn.onclick(set_properties)
turtle.mainloop()