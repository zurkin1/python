import turtle
screen = turtle.Screen()
screen.setup(700,700)
screen.bgcolor('cyan')

pen_size = turtle.numinput("What pen size do you want to design with?","Choose pen size")
pen_color = turtle.textinput("What color do you want to design with?","Choose pen color")
angle = turtle.numinput("What angle do you want to design with?","Choose angle")

line_length = 10
player = turtle.Turtle()
player.shape('blank')
player.pensize(pen_size)
player.pencolor(pen_color)

answer = turtle.textinput("Choose yes or no","What do you want to start painting?")
while answer == ('YES') or answer == ('Yes') or answer == ('yes') or answer == ('y'):
    player.forward(line_length)
    player.left(angle)
    line_length = line_length + 10
    answer = turtle.textinput("Choose yes or no", "What do you want to continue painting?")

turtle.mainloop()