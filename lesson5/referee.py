# -*- coding: utf-8 -*-
# ===================================================
# referee.py - השופט: מריץ את שני הבוטים אחד נגד השני 🏁
# ===================================================
# לפני ההרצה: שומרים את הקבצים של הקבוצות בשם team_a.py ו-team_b.py,
# באותה תיקייה עם bot_tools.py.
# השופט מעביר את ההודעות מבוט לבוט, עד שאחד מהם מנחש.
# ניחוש נכון = ניצחון (ומספר הצעדים), ניחוש שגוי = הפסד.

import random
import bot_tools
import team_a
import team_b


MAX_MESSAGES = 30 # רשת ביטחון: אם אף אחד לא ניחש אחרי 30 הודעות - תיקו
CORRECT_GUESS = "GUESS: BOT" # בקרב הזה שני הצדדים הם בוטים


def show(bot, message):
    print(bot.TEAM_NAME + ": " + message)
    print()


# מי פותח? אם שתי הקבוצות רוצות לפתוח (או ששתיהן לא) - מטילים מטבע
if team_a.STARTS_FIRST != team_b.STARTS_FIRST:
    if team_a.STARTS_FIRST:
        speaker, listener = team_a, team_b
    else:
        speaker, listener = team_b, team_a
else:
    speaker, listener = random.sample([team_a, team_b], 2)
print("=== " + team_a.TEAM_NAME + " vs " + team_b.TEAM_NAME + " ===")
print(speaker.TEAM_NAME + " starts.")
print()

message = bot_tools.respond(speaker, "")
show(speaker, message)
result = "Draw - no one guessed."
for i in range(MAX_MESSAGES):
    if bot_tools.is_guess(message):
        steps = bot_tools.turns(speaker) # כמה הודעות הבוט קיבל לפני שניחש
        if message == CORRECT_GUESS:
            result = speaker.TEAM_NAME + " WINS! Correct guess after " + str(steps) + " steps."
        else:
            result = speaker.TEAM_NAME + " guessed wrong - " + listener.TEAM_NAME + " WINS!"
        break
    reply = bot_tools.respond(listener, message)
    speaker, listener = listener, speaker # מחליפים תור
    message = reply
    show(speaker, message)

print("=== " + result + " ===")