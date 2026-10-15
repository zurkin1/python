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
# התור - חדש! 🆕 שני שחקנים מתחלפים
# ---------------------------------------------------
player = 1 # של מי התור: 1 או 2


def next_player():
    global player # כדי לשנות משתנה שנמצא מחוץ לפונקציה
    if player == 1:
        player = 2
    else:
        player = 1


def human_turn():
    title = "Player " + str(player)
    pile = screen.numinput(title, "Which pile? (1-" + str(len(piles)) + ")", minval=1, maxval=len(piles))
    if pile == None:
        return
    index = int(pile) - 1
    if piles[index] == 0:
        show_message("Pile " + str(index + 1) + " is empty! Try again")
        screen.ontimer(human_turn, 500)
        return
    count = screen.numinput(title, "How many tokens? (1-" + str(piles[index]) + ")", minval=1, maxval=piles[index])
    if count == None:
        return
    piles[index] = piles[index] - int(count)
    draw_board()
    if sum(piles) == 0: # השחקן הזה לקח את האסימון האחרון
        show_message("Player " + str(player) + " took the last token - LOSES!")
    else:
        next_player()
        show_message("Player " + str(player) + ", your turn")
        screen.ontimer(human_turn, 500)


draw_board()
show_message("Player 1, your turn")
screen.ontimer(human_turn, 500)
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שחקו משחק אחד נגד החבר שלידכם. מי ניצח?
# 2. שנו את ההודעה בסוף כך שתכתוב גם מי ניצח: "Player 2 WINS!"
# 3. שנו את החוק: מי שלוקח את האסימון האחרון - מנצח! (איזו שורה צריך לשנות?)
# 4. בונוס: נסו למצוא טריק: כשנשאר רק אסימון אחד בכל ערימה, כדאי להיות ראשון או שני?