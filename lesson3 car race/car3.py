# -*- coding: utf-8 -*-
# ===================================================
# car3.py - הכביש זז! לולאת המשחק 🎬
# ===================================================
# שלב 3: מכונית באה מולנו, והקווים זזים למטה - נראה כאילו אנחנו נוסעים!
# הסוד: הפונקציה game_loop מזיזה הכול קצת, ומבקשת לרוץ שוב בעוד 20 אלפיות שנייה.
# כמו ספר דפדוף - הרבה תמונות קטנות מהר = תנועה.

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

speed = 6 # כמה צעדים זזים בכל "תמונה"

def move_lines(): # חדש! 🆕
    for line in lines: # עוברים על כל הקווים ברשימה
        line.sety(line.ycor() - speed)
        if line.ycor() < -360:
            line.sety(line.ycor() + 720) # חוזר למעלה

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
# מכונית שבאה מולנו - חדש! 🆕
# ---------------------------------------------------
enemy = make_car("blue", random.choice(LANES), 450, 270)

def move_enemy():
    enemy.sety(enemy.ycor() - speed)
    if enemy.ycor() < -400: # יצאה מהמסך למטה
        enemy.sety(450) # חוזרת למעלה
        enemy.setx(random.choice(LANES)) # בנתיב אקראי

# ---------------------------------------------------
# לולאת המשחק - חדש! 🆕
# ---------------------------------------------------
def game_loop():
    move_lines()
    move_enemy()
    screen.update() # מציירים את המסך מחדש
    screen.ontimer(game_loop, 20) # עוד 20 אלפיות שנייה - שוב!

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

game_loop() # מתניעים! 🏁
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את speed ל-12. ול-2. מה ההבדל?
# 2. שנו את 20 ב-ontimer ל-100. מה קרה לתנועה? למה?
# 3. כל פעם שהמכונית חוזרת למעלה - תנו לה צבע אקראי:
#    enemy.shape(car_shape(random.choice(COLORS)))
# 4. בונוס: הוסיפו מכונית שנייה, enemy2, שמתחילה ב-y = 750.
