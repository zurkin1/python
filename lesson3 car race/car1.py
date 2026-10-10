# -*- coding: utf-8 -*-
# ===================================================
# car1.py - הכביש והמכונית שלנו 🛣️🚗
# ===================================================
# שלב 1: מציירים כביש עם 3 נתיבים ושמים עליו מכונית.
# הכול בנוי מפונקציות: draw_rect, draw_road, make_car

import turtle

screen = turtle.Screen()
screen.setup(500, 700)
screen.bgcolor("forestgreen")
screen.title("Car Race!")
screen.tracer(0) # מכבים ציור אוטומטי - הציור יופיע בבת אחת עם screen.update()

LANES = [-120, 0, 120] # רשימה: מיקום x של כל נתיב
ENEMIES = ["enemy_blue.gif", "enemy_yellow.gif", "enemy_purple.gif", "enemy_orange.gif", "enemy_pink.gif"]

# ---------------------------------------------------
# תמונות המכוניות - קבצי gif שנמצאים באותה תיקייה עם הקוד
# screen.register_shape adds a new shape to turtle’s list of shapes that turtles can wear.
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

def draw_rect(x, y, width, height, color): # 5 פרמטרים
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
    return car # מחזירים את המכונית החדשה

# ---------------------------------------------------
# הקווים המקווקווים - רשימה של צבים קטנים
# ---------------------------------------------------
lines = []
for x in [-60, 60]:
    for y in range(-360, 360, 80):
        line = turtle.Turtle()
        line.shape("square")
        line.color("white")
        line.shapesize(2, 0.3) # מלבן צר וארוך
        line.penup()
        line.goto(x, y)
        lines.append(line)

# ---------------------------------------------------
# התוכנית הראשית - קוראים לפונקציות
# ---------------------------------------------------
draw_road()
player = make_car("player.gif", LANES[1], -250) # הנתיב האמצעי

screen.update()
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. החליפו את התמונה של המכונית שלכם ל-"enemy_yellow.gif". למה היא נוסעת אחורה? 😄
# 2. שימו את המכונית בנתיב השמאלי: LANES[0]. ובנתיב הימני?
# 3. הוסיפו מכונית כחולה שנוסעת מולכם בנתיב אחר:
#    enemy = make_car("enemy_blue.gif", LANES[2], 200)
# 4. בונוס: הוסיפו עצים בצד הכביש - כתבו פונקציה draw_tree(x, y)
#    שמשתמשת ב-draw_rect לגזע ובעיגול (dot) לעלים.
