import turtle

wn = turtle.Screen()
wn.bgcolor('cyan')



def show_location(x,y):
    print(x,y)
def draw_window(player):
    for i in range(4):
        for i in range(4):
            player.forward(200)
            player.rt(90)
        player.rt(90)

#def draw_colors(player):



colors=['yellow','red','blue','green']
player = turtle.Turtle()
player.pensize(4)
player.color('navy')
draw_window(player)


wn.onclick(show_location)
turtle.mainloop()