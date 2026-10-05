#הגדרת פונקציה
#פונקציה שלא מקבלת ולא מחזירה ערך
import turtle


def print_good_morning():
    print("Good morning")

for i in range(5):
    print_good_morning()

#-----------------------------------
#פונקציה שמקבלת ערך ולא מחזירה
def print_name(name):
    print(name + " is great!")
print_name("Adam")
print_name("Noa")

#--------------------------------------------------------------
def check_grade(grade):
    if grade > 90:
        print("Excellent grade")
    elif grade > 80:
        print("Good")
    elif grade > 70:
        print("Do better next time")
    else:
        print("Talk to your teacher")

grade1 = 97
grade2 = 67
check_grade(grade1)
check_grade(grade2)

#-------------------------------------------------------
def greater(num1, num2):
    if num1>num2:
        print(str(num1) + " is greater")
    elif num2>num1:
        print(str(num2) + " is greater")
    else:
        print("two numbers are even")
greater(34, 35)
greater(3, 3)

#חזרה לספירלות
def draw_spiral(edges, angle):
    for i in range(edges):
        player.forward(10+i*5)
        player.right(angle)

player = turtle.Turtle()
player.color('red')
draw_spiral(15,89)

player.pu()
player.goto(200,200)
player.pd()
player.color('green')
draw_spiral(20,10)
turtle.mainloop()