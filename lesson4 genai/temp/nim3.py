# -*- coding: utf-8 -*-
# ===================================================
# nim3.py - משחקים נגד Gemini 🤖
# ===================================================
# שלב 3: שחקן 2 הוא Gemini! בתור שלו אנחנו שולחים לו את מצב המשחק
# ומבקשים תשובה של 2 מספרים: מספר ערימה וכמה אסימונים להוריד.
# Gemini יכול לטעות - לכן תמיד בודקים שהמהלך שלו חוקי.

import turtle
import random
from google import genai


screen = turtle.Screen()
screen.setup(600, 500)
screen.bgcolor("midnightblue")
screen.title("NIM")
screen.tracer(0)

# ---------------------------------------------------
# Gemini - חדש! 🆕
# ---------------------------------------------------
API_KEY = "" # המפתח שקיבלתם מהמורה
API_KEY = ""
MODEL = "gemini-3.6-flash"
client = genai.Client(api_key=API_KEY)

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
# Gemini - חדש! 🆕
# ---------------------------------------------------
def board_text(): # מצב המשחק כמחרוזת, למשל: "pile 1: 3 tokens"
    text = ""
    for index in range(len(piles)):
        text = text + "pile " + str(index + 1) + ": " + str(piles[index]) + " tokens\n" # \n = שורה חדשה
    return text


def ask_gemini():
    prompt = "You are a NIM player (https://en.wikipedia.org/wiki/Nim).\n"
    prompt = prompt + "Rules: in each turn a player removes 1 or more tokens from ONE pile.\n"
    prompt = prompt + "The player who takes the last token LOSES.\n"
    prompt = prompt + "This is the game now:\n" + board_text()
    prompt = prompt + "What is your best next move? Reply with 2 numbers only: x y\n"
    prompt = prompt + "x = the pile number, y = how many tokens to remove."
    print(prompt) # כדי שנראה מה שלחנו
    try: # נסה... ואם יש שגיאה - קפוץ ל-except במקום לקרוס
        response = client.models.generate_content(model=MODEL, contents=prompt)
        print("Gemini:", response.text)
        return response.text
    except Exception as error: # למשל: אין אינטרנט, מפתח שגוי, Gemini עמוס
        print("Gemini error:", error)
        return "" # תשובה ריקה = נשחק מהלך אקראי


def gemini_move(): # מחזירה רשימה: [index, count]
    parts = ask_gemini().split() # "2 3" -> ["2", "3"]
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit(): # isdigit = האם זה מספר?
        index = int(parts[0]) - 1
        count = int(parts[1])
        if index >= 0 and index < len(piles) and count >= 1 and count <= piles[index]: # מהלך חוקי?
            return [index, count]
    # Gemini טעה! תוכנית גיבוי: מהלך אקראי מערימה שאינה ריקה
    print("No legal move from Gemini - playing a random move instead")
    not_empty = []
    for index in range(len(piles)):
        if piles[index] > 0:
            not_empty.append(index)
    index = random.choice(not_empty)
    return [index, random.randint(1, piles[index])]


# ---------------------------------------------------
# המשחק - כמו בשלב 2, אבל השחקן השני הוא Gemini
# ---------------------------------------------------
MAX_TURNS = 30 # מספיק סיבובים לכל המשחק
draw_board()

for turn in range(MAX_TURNS): # בכל סיבוב: התור שלנו, ואז התור של Gemini
    if sum(piles) > 0: # sum = כמה אסימונים נשארו בסך הכול
        # התור שלנו - כמו בשלב 2
        pile = int(screen.numinput("Your turn", "Which pile? (1-3)", minval=1, maxval=3))
        index = pile - 1 # In python we count from 0.
        if piles[index] == 0:
            show_message("Pile " + str(pile) + " is empty! Try again") # try again
        else:
            count = int(screen.numinput("Your turn", "How many tokens?", minval=1, maxval=piles[index]))
            piles[index] = piles[index] - count
            draw_board()
            if sum(piles) == 0: # לקחנו את האסימון האחרון
                show_message("You took the last token - Gemini WINS!")
            else:
                # התור של Gemini
                show_message("Gemini is thinking...")
                move = gemini_move() # [index, count]
                piles[move[0]] = piles[move[0]] - move[1]
                draw_board()
                if sum(piles) == 0: # Gemini לקח את האסימון האחרון
                    show_message("Gemini took the last token - YOU WIN!")
                else:
                    show_message("Gemini took " + str(move[1]) + " from pile " + str(move[0] + 1))

turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שחקו 3 משחקים נגד Gemini. כמה ניצחתם? הסתכלו בחלון ההדפסות - מה Gemini ענה?
# 2. מחקו מה-prompt את השורה של החוקים (Rules). האם Gemini משחק טוב יותר או גרוע יותר?
# 3. שנו את ה-prompt כך ש-Gemini יענה בפורמט אחר, למשל "pile=2 take=3".
#    מה קורה למשחק? למה? (רמז: split ו-isdigit)
# 4. בונוס: שנו את MODEL למודל אחר (למשל gemini-pro-latest) - האם הוא משחק טוב יותר? האם הוא איטי יותר?