# -*- coding: utf-8 -*-
# ===================================================
# nim2.py - שני שחקנים, בדיקות, וסוף המשחק 👥
# ===================================================
# שלב 2: שחקן 1 ושחקן 2 משחקים בתורות על אותו מחשב.
# בודקים שהמהלך חוקי, ומי שלוקח את האסימון האחרון - מפסיד!

pile = 55
MAX_TAKE = 10
MAX_TURNS = 55 # מספיק תורות לכל המשחק (גם אם כל פעם לוקחים 1)


def legal_move(count): # מחזירה True אם מותר לקחת count אסימונים
    return count >= 1 and count <= MAX_TAKE and count <= pile


def player_turn(name): # התור של שחקן אנושי
    global pile # כדי לשנות משתנה שנמצא מחוץ לפונקציה
    print()
    print("*" * pile)
    print("Tokens left: " + str(pile))
    count = int(input(name + ", how many tokens do you take? "))
    if not legal_move(count): # חדש! 🆕 בודקים את המהלך
        print("Illegal move! You take 1 token.")
        count = 1
    pile = pile - count
    if pile == 0: # חדש! 🆕 סוף המשחק
        print(name + " took the last token - " + name + " LOSES!")


print("Let's play NIM!")
print("Take 1 to " + str(MAX_TAKE) + " tokens in each turn. Who takes the last token - LOSES!")

for turn in range(MAX_TURNS):
    if pile > 0: # המשחק עוד לא נגמר
        player_turn("Player 1")
    if pile > 0:
        player_turn("Player 2")

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שחקו משחק אחד נגד החבר שלידכם. מי ניצח?
# 2. שנו את ההודעה בסוף כך שתכתוב גם מי ניצח: "Player 2 WINS!"
#    (רמז: הוסיפו לפונקציה פרמטר שני - השם של היריב)
# 3. שנו את החוק: מי שלוקח את האסימון האחרון - מנצח! (איזו שורה צריך לשנות?)
# 4. בונוס: יש טריק שבעזרתו השחקן הראשון תמיד מנצח. רמז: כמה אסימונים כדאי להשאיר ליריב?