# -*- coding: utf-8 -*-
# ===================================================
# turtle5.py - צובעים צורות וכותבים טקסט 🏠
# ===================================================

import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# --- קירות הבית: ריבוע צבוע ---
t.penup()
t.goto(-100, -150)
t.pendown()
t.color("black", "khaki") # צבע ראשון = קו, צבע שני = מילוי
t.begin_fill() # מתחילים לצבוע מכאן...
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill() # ...ועד כאן - הצורה נצבעת!


# --- גג: משולש אדום ---
t.penup()
t.goto(-120, 50)
t.pendown()
t.color("darkred", "red")
t.begin_fill()
for i in range(3):
    t.forward(240)
    t.left(120)
t.end_fill()


# --- דלת ---
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


# --- שמש בפינה ---
t.penup()
t.goto(230, 150)
t.pendown()
t.color("orange", "yellow")
t.begin_fill()
t.circle(40)
t.end_fill()


# --- כיתוב ---
t.penup()
t.goto(0, -220)
t.color("darkblue")
t.write("My Home", align="center", font=("Arial", 24, "bold")) # כותבים טקסט על המסך
t.hideturtle()


turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. הוסיפו חלון: ריבוע קטן בצבע "lightblue" בצד ימין של הבית.
# 2. שנו את הכיתוב לשם שלכם (באנגלית) ואת הגופן ל-"Courier".
# 3. ציירו דשא: מלבן ירוק צבוע בתחתית המסך.
# 4. בונוס: ציירו עץ ליד הבית - גזע חום (מלבן) וצמרת ירוקה (עיגול).
