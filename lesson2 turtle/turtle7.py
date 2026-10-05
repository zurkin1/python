# -*- coding: utf-8 -*-
# ===================================================
# turtle7.py - שולטים בצב עם המקלדת ⌨️
# ===================================================
# הצב מצייר לאן שאתם מזיזים אותו - כמו לוח ציור מגנטי!
# חיצים = תזוזה, רווח = הרם/הורד עט, c = מחק הכול

import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Drive the turtle with the arrow keys")

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(3)
t.speed(0)

# פונקציה (def) = שם לקבוצת פקודות. נלמד עליהן לעומק בהמשך
def go_up():
    t.setheading(90) # מסתכלים למעלה
    t.forward(20)

def go_down():
    t.setheading(270) # מסתכלים למטה
    t.forward(20)

def go_left():
    t.setheading(180) # מסתכלים שמאלה
    t.forward(20)

def go_right():
    t.setheading(0) # מסתכלים ימינה
    t.forward(20)

def toggle_pen():
    if t.isdown(): # אם העט למטה - מרימים אותו
        t.penup()
    else:
        t.pendown()

def clear_all():
    #t.clear() # מוחקים את הציור (הצב נשאר במקום)
    screen.clear()
    screen.bgcolor("lightyellow")
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.pensize(3)
    t.speed(0)
    

# מחברים מקשים לפונקציות
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(toggle_pen, "space")
screen.onkey(clear_all, "c")
screen.listen() # מתחילים "להקשיב" למקלדת

turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את גודל הצעד מ-20 ל-40. מה השתנה?
# 2. הוסיפו מקש r שהופך את צבע העט לאדום: t.color("red")
# 3. הוסיפו מקש b שהופך את צבע העט לכחול.
# 4. בונוס: הוסיפו מקש + שמגדיל את עובי העט (רמז: t.pensize(t.pensize() + 1)).
