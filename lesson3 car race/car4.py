# -*- coding: utf-8 -*-
# ===================================================
# car4.py - בום! זיהוי התנגשות 💥
# ===================================================
# שלב 4: אם המכונית שלנו נוגעת במכונית אחרת - המשחק נגמר.
# הפונקציה crashed מחזירה (return) תשובה: True או False

import turtle
import random

screen = turtle.Screen()
screen.setup(500, 700)
screen.bgcolor("forestgreen")
screen.title("Car Race!")
screen.tracer(0)

LANES = [-120, 0, 120] # רשימה: מיקום x של כל נתיב
COLORS = ["red", "blue", "yellow", "purple", "orange", "pink"]

# ---------------------------------------------------
# צורת מכונית - קוד מוכן, לא חייבים להבין אותו 🙂
# ---------------------------------------------------
def car_shape(color):
    name = "car_" + color
    if name not in screen.getshapes():
        car = turtle.Shape("compound")
        for x in [-23, 17]: # גלגלים
            for y in [-26, 14]:
                car.addcomponent(((x, y), (x + 6, y), (x + 6, y + 12), (x, y + 12)), "black")
        car.addcomponent(((-18, -32), (18, -32), (18, 32), (-18, 32)), color, "black") # גוף
        car.addcomponent(((-14, 6), (14, 6), (11, 18), (-11, 18)), "lightblue", "black") # שמשה קדמית
        car.addcomponent(((-13, -24), (13, -24), (11, -16), (-11, -16)), "lightblue", "black") # שמשה אחורית
        screen.register_shape(name, car)
    return name

# ---------------------------------------------------
# פונקציות ציור
# ---------------------------------------------------
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

def draw_rect(x, y, width, height, color):
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

def draw_road():
    draw_rect(-180, -350, 360, 700, "dimgray") # הכביש
    draw_rect(-186, -350, 6, 700, "white") # שוליים משמאל
    draw_rect(180, -350, 6, 700, "white") # שוליים מימין

def make_car(color, x, y, heading):
    car = turtle.Turtle()
    car.shape(car_shape(color))
    car.penup()
    car.setheading(heading) # 90 = למעלה, 270 = למטה
    car.goto(x, y)
    return car

# ---------------------------------------------------
# הקווים המקווקווים - רשימה של צבים קטנים
# ---------------------------------------------------
lines = []
for x in [-60, 60]:
    for y in range(-360, 360, 80):
        line = turtle.Turtle()
        line.shape("square")
        line.color("white")
        line.shapesize(2, 0.3)
        line.penup()
        line.goto(x, y)
        lines.append(line)

speed = 6

def move_lines():
    for line in lines:
        line.sety(line.ycor() - speed)
        if line.ycor() < -360:
            line.sety(line.ycor() + 720)

# ---------------------------------------------------
# השחקן
# ---------------------------------------------------
draw_road()
lane = 1
player = make_car("red", LANES[lane], -250, 90)

def move_left():
    global lane
    if lane > 0:
        lane = lane - 1
        player.setx(LANES[lane])

def move_right():
    global lane
    if lane < len(LANES) - 1:
        lane = lane + 1
        player.setx(LANES[lane])

# ---------------------------------------------------
# מכונית שבאה מולנו
# ---------------------------------------------------
enemy = make_car("blue", random.choice(LANES), 450, 270)

def move_enemy():
    enemy.sety(enemy.ycor() - speed)
    if enemy.ycor() < -400:
        enemy.sety(450)
        enemy.setx(random.choice(LANES))
        enemy.shape(car_shape(random.choice(COLORS)))

# ---------------------------------------------------
# זיהוי התנגשות - חדש! 🆕
# ---------------------------------------------------
def crashed(car1, car2): # מחזירה True אם המכוניות נוגעות
    close_x = abs(car1.xcor() - car2.xcor()) < 36 # רוחב מכונית
    close_y = abs(car1.ycor() - car2.ycor()) < 64 # אורך מכונית
    return close_x and close_y

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("yellow")

# ---------------------------------------------------
# לולאת המשחק
# ---------------------------------------------------
def game_loop():
    move_lines()
    move_enemy()
    screen.update()
    if crashed(player, enemy): # 💥
        writer.write("CRASH!", align="center", font=("Arial", 40, "bold"))
        screen.update()
    else:
        screen.ontimer(game_loop, 20) # ממשיכים רק אם לא התנגשנו

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

game_loop()
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את 36 ל-100 בפונקציה crashed. מה קורה? למה?
# 2. כשיש התנגשות - שנו את צבע המסך לאדום: screen.bgcolor("red")
# 3. הוסיפו מתחת ל-CRASH! את המשפט "Try again!" (בגודל קטן יותר).
# 4. בונוס: הוסיפו משתנה score שגדל ב-1 בכל פעם שהמכונית יוצאת מהמסך למטה.
#    (רמז: global score בתוך move_enemy)
