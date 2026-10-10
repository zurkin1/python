# -*- coding: utf-8 -*-
# ===================================================
# functions_demo.py - פונקציות: מלמדים את פייתון מילה חדשה 🧩
# ===================================================

import turtle

t = turtle.Turtle()
t.speed(0)

# --- 1. פונקציה עם פרמטרים ---
def draw_square(size, color): # size, color = פרמטרים
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# --- 2. פונקציה שקוראת לפונקציה אחרת ---
def draw_house(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_square(80, color) # הקירות
    t.goto(x, y + 80) # הגג
    t.color("brown")
    t.begin_fill()
    t.goto(x + 40, y + 130)
    t.goto(x + 80, y + 80)
    t.goto(x, y + 80)
    t.end_fill()

# --- 3. פונקציה שמחזירה ערך (return) ---
def area(width, height):
    result = width * height # result = משתנה מקומי, קיים רק בתוך הפונקציה
    return result

# --- התוכנית הראשית: קריאות לפונקציות ---
draw_house(-250, -50, "khaki")
draw_house(-100, -50, "lightblue")
draw_house(50, -50, "pink")

t.hideturtle()
turtle.done()
