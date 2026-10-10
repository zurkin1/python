# -*- coding: utf-8 -*-
# ===================================================
# car2.py - נוהגים עם החיצים ⌨️🚗
# ===================================================
# שלב 2: חץ שמאלה / ימינה = המכונית עוברת נתיב.
# המשתנה lane שומר באיזה נתיב אנחנו: 0, 1 או 2 (אינדקס ברשימה LANES)

import turtle

screen = turtle.Screen()
screen.setup(500, 700)
screen.bgcolor("forestgreen")
screen.title("Car Race!")
screen.tracer(0)

LANES = [-120, 0, 120] # רשימה: מיקום x של כל נתיב
ENEMIES = ["enemy_blue.gif", "enemy_yellow.gif", "enemy_purple.gif", "enemy_orange.gif", "enemy_pink.gif"]

# ---------------------------------------------------
# תמונות המכוניות - קבצי gif שנמצאים באותה תיקייה עם הקוד
# ---------------------------------------------------
screen.register_shape("player.gif") # המכונית שלנו (פונה למעלה)
for image in ENEMIES: # המכוניות שבאות מולנו (פונות למטה)
    screen.register_shape(image)

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

def make_car(image, x, y):
    car = turtle.Turtle()
    car.shape(image) # התמונה היא הצורה של הצב
    car.penup()
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

# ---------------------------------------------------
# השחקן - חדש! 🆕
# ---------------------------------------------------
draw_road()
lane = 1 # האינדקס של הנתיב ברשימה LANES (0, 1 או 2)
player = make_car("player.gif", LANES[lane], -250)

def move_left():
    global lane # כדי לשנות משתנה שנמצא מחוץ לפונקציה
    if lane > 0: # לא יוצאים מהכביש!
        lane = lane - 1
        player.setx(LANES[lane])
        screen.update()

def move_right():
    global lane
    if lane < len(LANES) - 1: # len(LANES) - 1 = האינדקס האחרון
        lane = lane + 1
        player.setx(LANES[lane])
        screen.update()

screen.listen() # המסך "מקשיב" למקלדת
screen.onkey(move_left, "Left") # חץ שמאלה -> move_left
screen.onkey(move_right, "Right") # חץ ימינה -> move_right

screen.update()
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. מה קורה אם מוחקים את התנאי if lane > 0 ? נסו ללחוץ הרבה שמאלה.
# 2. הוסיפו את המקשים a ו-d (כמו במשחקי מחשב) - אותן פונקציות!
# 3. הוסיפו נתיב רביעי לרשימה LANES. האם move_right עדיין עובדת? למה?
# 4. בונוס: מקש למעלה מזיז את המכונית קדימה ב-20 (player.sety)
