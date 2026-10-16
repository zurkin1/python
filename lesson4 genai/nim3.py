# -*- coding: utf-8 -*-
# ===================================================
# nim3.py - משחקים נגד Gemini 🤖
# ===================================================
# שלב 3: השחקן השני הוא Gemini! בתור שלו שולחים לו את מצב המשחק
# ומבקשים תשובה של מספר אחד: כמה אסימונים לקחת.
# Gemini יכול לטעות - לכן תמיד בודקים שהמהלך שלו חוקי.

import random
from google import genai


API_KEY = "PUT-YOUR-API-KEY-HERE" # המפתח שקיבלתם מהמורה
MODEL = "gemini-3.6-flash"
client = genai.Client(api_key=API_KEY)

pile = 55
MAX_TAKE = 10
MAX_TURNS = 55


def legal_move(count):
    return count >= 1 and count <= MAX_TAKE and count <= pile


def player_turn(name): # כמו בשלב 2
    global pile
    print()
    print("*" * pile)
    print("Tokens left: " + str(pile))
    count = int(input(name + ", how many tokens do you take? "))
    if not legal_move(count):
        print("Illegal move! You take 1 token.")
        count = 1
    pile = pile - count
    if pile == 0:
        print(name + " took the last token - " + name + " LOSES!")


# ---------------------------------------------------
# Gemini - חדש! 🆕
# ---------------------------------------------------
def ask_gemini():
    prompt = "You are a NIM player (https://en.wikipedia.org/wiki/Nim).\n"
    prompt = prompt + "There is one pile with " + str(pile) + " tokens.\n"
    prompt = prompt + "In each turn a player takes 1 to " + str(MAX_TAKE) + " tokens.\n"
    prompt = prompt + "The player who takes the last token LOSES.\n"
    prompt = prompt + "How many tokens do you take? Reply with one number only."
    print("Sending to Gemini:") # כדי שנראה מה שלחנו
    print(prompt)
    try: # נסה... ואם יש שגיאה - קפוץ ל-except במקום לקרוס
        response = client.models.generate_content(model=MODEL, contents=prompt)
        print("Received from Gemini: " + response.text) # מה חזר
        return response.text
    except Exception as error: # למשל: אין אינטרנט, מפתח שגוי, Gemini עמוס
        print("Gemini error:", error)
        return "" # תשובה ריקה = נשחק מהלך אקראי


def gemini_turn():
    global pile
    print()
    print("Gemini is thinking...")
    answer = ask_gemini().strip() # strip = מוחקים רווחים וירידות שורה מהקצוות
    if answer.isdigit() and legal_move(int(answer)): # isdigit = האם זה מספר?
        count = int(answer)
    else: # Gemini טעה! תוכנית גיבוי: מהלך אקראי
        print("Not a legal move - Gemini takes a random number instead")
        count = random.randint(1, MAX_TAKE)
        if count > pile:
            count = pile
    pile = pile - count
    print("Gemini took " + str(count) + " tokens")
    if pile == 0:
        print("Gemini took the last token - YOU WIN!")


print("Let's play NIM against Gemini!")
print("Take 1 to " + str(MAX_TAKE) + " tokens in each turn. Who takes the last token - LOSES!")

for turn in range(MAX_TURNS):
    if pile > 0:
        player_turn("You")
    if pile > 0:
        gemini_turn() # במקום Player 2

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שחקו 3 משחקים נגד Gemini. כמה ניצחתם? מה Gemini ענה בכל תור?
# 2. מחקו מה-prompt את השורה של החוקים (LOSES). האם Gemini משחק טוב יותר או גרוע יותר?
# 3. שנו את ה-prompt כך ש-Gemini יענה במשפט, למשל "I take 3 tokens".
#    מה קורה למשחק? למה? (רמז: isdigit)
# 4. בונוס: שנו את MODEL למודל אחר (למשל gemini-pro-latest) - האם הוא משחק טוב יותר? האם הוא איטי יותר?