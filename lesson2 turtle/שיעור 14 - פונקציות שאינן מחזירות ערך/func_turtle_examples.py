import turtle

def draw_squere(player):
    for i in range(4):
        player.forward(100)
        player.right(90)

def draw_triangle(player, steps):
    for i in range(3):
        player.forward(steps)
        player.right(120)

p = turtle.Turtle()
draw_squere(p)
draw_triangle(p,40)


turtle.mainloop()