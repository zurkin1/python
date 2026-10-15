# -*- coding: utf-8 -*-
# ===================================================
# nim2.py - שני שחקנים, ומי שלוקח אחרון מפסיד 👥
# ===================================================
# שלב 2: שחקן 1 ושחקן 2 משחקים בתורות על אותו מחשב.
# המשתנה player שומר של מי התור. מי שלוקח את האסימון האחרון - מפסיד!

import turtle


screen = turtle.Screen()
screen.setup(600, 500)
screen.bgcolor("midnightblue")
screen.title("NIM")
screen.tracer(0)

piles = [3, 4, 5] # רשימה: כמה אסימונים יש בכל ערימה
COLORS = ["orange", "deepskyblue", "hotpink"] # צבע לכל ערימה
ROWS = [80, -20, -120] # מיקום y של כל ערימה

# ---------------------------------------------------
# פונקציות ציור
# ---------------------------------------------------
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


def draw_rect(x, y, width, height, color):
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
# המשחק - חדש! 🆕 לולאה: בכל סיבוב תור אחד
# ---------------------------------------------------
MAX_TURNS = 30 # מספיק תורות לכל המשחק
player = 0 # של מי התור
draw_board()

for turn in range(MAX_TURNS):
    if sum(piles) > 0: # sum = כמה אסימונים נשארו בסך הכול
        # First question
        pile = int(screen.numinput("Player " + str(player+1), "Which pile? (1-3)", minval=1, maxval=3))
        index = pile - 1 # In python we count from 0.
        if piles[index] == 0:
            show_message("Pile " + str(pile) + " is empty! Try again") # try again
        else:
            # Second question
            count = int(screen.numinput("Player " + str(player+1), "How many tokens?", minval=1, maxval=piles[index]))
            piles[index] = piles[index] - count
            draw_board()
            if sum(piles) == 0: # השחקן הזה לקח את האסימון האחרון
                show_message("Player " + str(player+1) + " took the last token - LOSES!")
            else:
                player = 1-player # מחליפים תור

turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שחקו משחק אחד נגד החבר שלידכם. מי ניצח?
# 2. שנו את ההודעה בסוף כך שתכתוב גם מי ניצח: "Player 2 WINS!"
# 3. שנו את החוק: מי שלוקח את האסימון האחרון - מנצח! (איזו שורה צריך לשנות?)
# 4. בונוס: נסו למצוא טריק: כשנשאר רק אסימון אחד בכל ערימה, כדאי להיות ראשון או שני?