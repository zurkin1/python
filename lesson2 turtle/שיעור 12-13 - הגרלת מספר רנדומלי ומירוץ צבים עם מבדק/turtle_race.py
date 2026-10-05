import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("cyan")

# Create two turtles
turtle_1 = turtle.Turtle()
turtle_1.color("red")
turtle_1.shape("turtle")
turtle_1.penup()
turtle_1.goto(-200, 100)

'''
turtle_2 = turtle.Turtle()
turtle_2.color("blue")
turtle_2.shape("turtle")
turtle_2.penup()
turtle_2.goto(-200, -100)
'''
# Draw the finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(200, 150)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(300)
finish_line.hideturtle()

while turtle_1.xcor() < 200 :
    distance = random.randint(1, 10)
    turtle_1.forward(distance)

'''
# Run the race
while turtle_1.xcor() < 200 and turtle_2.xcor() < 200:
    distance = random.randint(1, 10)
    turtle_1.forward(distance)
    distance = random.randint(1, 10)
    turtle_2.forward(distance)

# Check who won
if turtle_1.xcor() > turtle_2.xcor():
    print("Red turtle wins!")
else:
    print("Blue turtle wins!")
'''
# Close the window on click
turtle.mainloop()