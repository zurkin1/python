
import random
import turtle
tr = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('beige')
wn.setup(800,600)
wn.addshape('bird.gif')
tr.shape('bird.gif')

baloon_image_list = ['red.gif','pink.gif','green.gif','yellow.gif']
for img in baloon_image_list:
    wn.addshape(img)
baloons_on_screen = []

while True:
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    rand_image = random.choice(baloon_image_list)
    t = turtle.Turtle()
    t.pu()
    t.shape('blank')
    t.goto(x,y)
    t.shape(rand_image)
    baloons_on_screen.append(t)
wn.mainloop()