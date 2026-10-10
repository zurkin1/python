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

def make_car(color, x, y, heading):
    car = turtle.Turtle()
    car.shape(car_shape(color))
    car.penup()
    car.setheading(heading) # 90 = למעלה, 270 = למטה
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
player = make_car("red", LANES[1], -250, 90) # הנתיב האמצעי

screen.update()
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את צבע המכונית שלכם.
# 2. שימו את המכונית בנתיב השמאלי: LANES[0]. ובנתיב הימני?
# 3. הוסיפו מכונית כחולה שנוסעת מולכם (heading = 270) בנתיב אחר:
#    enemy = make_car("blue", LANES[2], 200, 270)
# 4. בונוס: הוסיפו עצים בצד הכביש - כתבו פונקציה draw_tree(x, y)
#    שמשתמשת ב-draw_rect לגזע ובעיגול (dot) לעלים.
