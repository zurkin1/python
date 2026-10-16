# -*- coding: utf-8 -*-
# ===================================================
# nim1.py - הלוח והתור שלנו 🪙
# ===================================================
# שלב 1: מציירים 3 ערימות של אסימונים, ובכל תור מורידים אסימונים מערימה אחת.
# הערימות שמורות ברשימה: piles[0] = כמה אסימונים יש בערימה 1

import turtle


screen = turtle.Screen()
screen.setup(600, 500)
screen.bgcolor("midnightblue")
screen.title("NIM")
screen.tracer(0) # מכבים ציור אוטומטי - הציור יופיע בבת אחת עם screen.update()

piles = [3, 4, 5] # רשימה: כמה אסימונים יש בכל ערימה
COLORS = ["orange", "deepskyblue", "hotpink"] # צבע לכל ערימה
ROWS = [80, -20, -120] # מיקום y של כל ערימה

# ---------------------------------------------------
# פונקציות ציור
# ---------------------------------------------------
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


def draw_rect(x, y, width, height, color): # מכירים משיעור 3!
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


def draw_pile(index): # index = המיקום של הערימה ברשימה (0, 1 או 2)
    y = ROWS[index]
    pen.goto(-260, y + 5)
    pen.color("white")
    pen.write("Pile " + str(index + 1), font=("Arial", 18, "bold")) # לאנשים סופרים מ-1
    for i in range(piles[index]): # אסימון אחד לכל מספר ברשימה
        draw_rect(-150 + i * 55, y, 40, 40, COLORS[index])


def draw_board():
    pen.clear() # מוחקים את הציור הקודם
    for index in range(len(piles)):
        draw_pile(index)
    screen.update()


# ---------------------------------------------------
# הודעות למעלה במסך
# ---------------------------------------------------
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("yellow")



draw_board()

turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את הרשימה piles ל-[1, 3, 5]. מה השתנה בלוח?
# 2. שנו את הצבעים ברשימה COLORS לצבעים שאתם אוהבים.
# 3. מה יקרה אם תבחרו בערימה ריקה? מצאו בקוד את ה-if שמטפל בזה.
# 4. בונוס: הוסיפו ערימה רביעית עם 7 אסימונים (צריך לשנות 3 רשימות!).