# -*- coding: utf-8 -*-
# ===================================================
# functions_demo.py - פונקציות: מלמדים את פייתון מילה חדשה 🧩
# ===================================================

import turtle

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
#screen.bgcolor("black")

# --- 1. פונקציה עם פרמטרים ---
def draw_square(size, color): # size, color = פרמטרים
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# --- 2. פונקציה שקוראת לפונקציה אחרת ---
def draw_house(x, y, color, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_square(size, color) # הקירות
    t.goto(x, y + size) # הגג
    t.color("brown")
    t.begin_fill()
    t.goto(x + 40, y + 130)
    t.goto(x + size, y + size)
    t.goto(x, y + size)
    t.end_fill()

# --- 3. פונקציה שמחזירה ערך (return) ---
def area(width, height):
    result = width * height # result = משתנה מקומי, קיים רק בתוך הפונקציה
    return result

def draw_sun(x , y, size_sun):
    # Sun
    t.begin_fill()
    t.penup() # מרימים את העט - זזים בלי לצייר
    t.goto(x, y) # קופצים לנקודה (x=0, y=-100)
    t.pendown() # מורידים את העט - שוב מציירים
    t.color("yellow")
    t.circle(size_sun)
    t.end_fill()

# --- התוכנית הראשית: קריאות לפונקציות ---
size = screen.numinput("Question", "size? (50-100)", default=80, minval=50, maxval=100) # חלון קלט
draw_house(-250, -50, "khaki", size)
draw_house(-100, -50, "lightblue", size)
draw_house(50, -50, "pink", size)
draw_house(150, -50, "yellow", size)

draw_sun(-200, 200, 50)

t.hideturtle()
turtle.done()
