# -*- coding: utf-8 -*-
# ===================================================
# turtle_game.py - משחק: תפסו את הצב! 🎮🐢
# ===================================================
# הצב קופץ למקומות אקראיים. לחצו עליו עם העכבר כדי לקבל נקודה.
# יש לכם 30 שניות - כמה נקודות תצליחו לצבור?

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Catch the turtle!")
screen.setup(700, 560)

# --- הצב שצריך לתפוס ---
player = turtle.Turtle()
player.shape("turtle")
player.color("darkgreen")
player.shapesize(2) # צב גדול פי 2
player.speed(0) # קפיצה מיידית בלי אנימציה
player.penup()

# --- הצב שכותב את הניקוד ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

score = 0 # משתנה: הניקוד
time_left = 30 # משתנה: כמה שניות נשארו
game_over = False

def show_text():
    pen.clear()
    pen.goto(0, 240)
    pen.write("Score: " + str(score) + "    Time: " + str(time_left), align="center", font=("Arial", 20, "bold"))

def jump():
    x = random.randint(-300, 300) # מקום אקראי במסך
    y = random.randint(-230, 200)
    player.goto(x, y)

def caught(x, y): # נקראת בכל לחיצה על הצב
    global score # כדי לשנות משתנה שנמצא מחוץ לפונקציה
    if not game_over:
        score = score + 1
        player.color(random.choice(["darkgreen", "blue", "purple", "orange", "red"]))
        jump()
        show_text()

def tick(): # נקראת פעם בשנייה - השעון של המשחק
    global time_left, game_over
    time_left = time_left - 1
    show_text()
    if time_left > 0:
        if random.randint(1, 2) == 1: # בערך פעם בשתי שניות הצב בורח לבד
            jump()
        screen.ontimer(tick, 1000) # עוד שנייה - שוב tick
    else:
        game_over = True
        player.hideturtle()
        pen.goto(0, 0)
        if score >= 15:
            pen.write("Amazing! " + str(score) + " points!", align="center", font=("Arial", 32, "bold"))
        else:
            pen.write("Game over: " + str(score) + " points", align="center", font=("Arial", 32, "bold"))

player.onclick(caught) # לחיצה על הצב -> הפונקציה caught
show_text()
jump()
screen.ontimer(tick, 1000) # מפעילים את השעון
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את זמן המשחק ל-20 שניות. קשה יותר?
# 2. הקטינו את הצב: player.shapesize(1)
# 3. שנו את התנאי כך ש-"Amazing!" יופיע רק מ-20 נקודות.
# 4. בונוס: בכל לחיצה, הקטינו את הצב קצת - המשחק נהיה קשה יותר!
