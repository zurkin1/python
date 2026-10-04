# -*- coding: utf-8 -*-
# ===================================================
# פתרון לדוגמה לשיעורי הבית - למורה בלבד (לא לשתף עם התלמידים)
# ===================================================

import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

time_of_day = "night" # "day" או "night"

# 1. צבע רקע (+ סעיף בחירה א')
if time_of_day == "day":
    screen.bgcolor("lightblue")
else:
    screen.bgcolor("midnightblue")

# דשא
t.penup()
t.goto(-350, -280)
t.pendown()
t.color("green", "forestgreen")
t.begin_fill()
for i in range(2):
    t.forward(700)
    t.left(90)
    t.forward(130)
    t.left(90)
t.end_fill()

# 2. הבית - קירות
t.penup()
t.goto(-100, -150)
t.pendown()
t.color("black", "khaki")
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# גג
t.penup()
t.goto(-120, 50)
t.pendown()
t.color("darkred", "firebrick")
t.begin_fill()
for i in range(3):
    t.forward(240)
    t.left(120)
t.end_fill()

# דלת
t.penup()
t.goto(-25, -150)
t.pendown()
t.color("black", "saddlebrown")
t.begin_fill()
for i in range(2):
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# 3. שמש או ירח
t.penup()
t.goto(230, 140)
t.pendown()
if time_of_day == "day":
    t.color("orange", "yellow")
else:
    t.color("white", "lightyellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# ג'. כוכבים אקראיים בלילה
if time_of_day == "night":
    t.penup()
    for i in range(30):
        t.goto(random.randint(-330, 330), random.randint(80, 260))
        t.dot(random.randint(3, 7), "white")

# 6. השם שלי
t.penup()
t.goto(0, -230)
t.color("white")
t.write("Noa's House", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()
