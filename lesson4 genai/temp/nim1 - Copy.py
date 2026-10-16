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


def show_message(text):
    writer.clear()
    writer.goto(0, 170)
    writer.write(text, align="center", font=("Arial", 18, "bold"))
    screen.update()


# ---------------------------------------------------
# התור - שואלים מאיזו ערימה ומה הכמות
# ---------------------------------------------------
def human_turn():
    pile = screen.numinput("Your turn", "Which pile? (1-" + str(len(piles)) + ")", minval=1, maxval=len(piles))
    if pile == None: # לחצו Cancel - עוצרים
        return
    index = int(pile) - 1 # numinput מחזיר 2.0 - int הופך אותו ל-2. ואז 1- כי האינדקס מתחיל מ-0
    if piles[index] == 0:
        show_message("Pile " + str(index + 1) + " is empty! Try again")
        screen.ontimer(human_turn, 500)
        return
    count = screen.numinput("Your turn", "How many tokens? (1-" + str(piles[index]) + ")", minval=1, maxval=piles[index])
    if count == None:
        return
    piles[index] = piles[index] - int(count) # מורידים אסימונים מהערימה
    draw_board()
    if sum(piles) == 0: # sum = סכום כל המספרים ברשימה
        show_message("No tokens left!")
    else:
        show_message("Tokens left: " + str(sum(piles)))
        screen.ontimer(human_turn, 500) # עוד חצי שנייה - שוב התור שלנו


draw_board()
show_message("Let's play NIM!")
screen.ontimer(human_turn, 500)
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את הרשימה piles ל-[1, 3, 5]. מה השתנה בלוח?
# 2. שנו את הצבעים ברשימה COLORS לצבעים שאתם אוהבים.
# 3. מה יקרה אם תבחרו בערימה ריקה? מצאו בקוד את ה-if שמטפל בזה.
# 4. בונוס: הוסיפו ערימה רביעית עם 7 אסימונים (צריך לשנות 3 רשימות!).