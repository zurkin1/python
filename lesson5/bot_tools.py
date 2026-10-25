# -*- coding: utf-8 -*-
# ===================================================
# bot_tools.py - כלים מוכנים לבוט 🧰 (לא צריך לשנות את הקובץ הזה!)
# ===================================================
# כאן נמצא כל מה שקבוע: שליחה ל-Gemini, ההיסטוריה של השיחה, בדיקת התשובות
# (30 מילים, פורמט הניחוש) והמשחק. הבוט שלכם נמצא בקובץ turing_bot.py
#
# כדי לבדוק את הבוט: מריצים את הקובץ הזה (bot_tools.py).
# הבוט כותב, ואתם מקלידים את התשובות של הצד השני - כאילו אתם היריב.

import random
from google import genai
from google.genai import types


API_KEY = "PUT-YOUR-API-KEY-HERE" # המפתח שקיבלתם מהמורה
MODEL = "gemini-3.6-flash"
MAX_WORDS = 30 # כל הודעה - עד 30 מילים
MAX_TURNS = 8 # בתור הזה חייבים לנחש

client = genai.Client(api_key=API_KEY)
games = {} # המצב של כל בוט: השיחה (history), כמה הודעות קיבלנו (turn) וכמה שלחנו (sent)


def ask_gemini(system, prompt, temperature=0.7):
    # שולחים ל-Gemini הוראות מערכת (system) ובקשה (prompt), ומחזירים את התשובה
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(system_instruction=system, temperature=temperature))
        return response.text.strip()
    except Exception as error: # אין אינטרנט, מפתח שגוי, Gemini עמוס...
        print("Gemini error:", error)
        return ""


def history_text(history):
    # כל השיחה כמחרוזת אחת - כדי לשלוח אותה ל-Gemini
    return "\n".join(history)


def clean_reply(reply):
    # בודקים את ההודעה: ניחוש בפורמט הנכון, או הודעה של עד 30 מילים
    if "GUESS:" in reply.upper():
        if "HUMAN" in reply.upper():
            return "GUESS: HUMAN"
        if "BOT" in reply.upper():
            return "GUESS: BOT"
    words = reply.split()
    if len(words) == 0:
        return "סליחה, לא הבנתי. אתה יכול להגיד את זה שוב?" # אין תשובה - משפט גיבוי
    return " ".join(words[:MAX_WORDS]) # חותכים ל-30 מילים


def is_guess(message):
    return message.startswith("GUESS:")


def respond(bot, their_message):
    # תור אחד של הבוט: מקבלים את ההודעה של הצד השני ("" אם הבוט פותח) ומחזירים את ההודעה של הבוט
    if bot.__name__ not in games:
        games[bot.__name__] = {"history": [], "turn": 0, "sent": 0}
    game = games[bot.__name__]
    if their_message != "":
        game["history"].append("Other: " + their_message)
        game["turn"] = game["turn"] + 1
    message = clean_reply(bot.decide(game["history"], game["turn"], game["sent"]))
    if game["turn"] >= MAX_TURNS and not is_guess(message): # בתור 8 חייבים לנחש
        message = random.choice(["GUESS: HUMAN", "GUESS: BOT"])
    game["history"].append("Me: " + message)
    game["sent"] = game["sent"] + 1
    return message


def turns(bot):
    # כמה הודעות הבוט קיבל מהצד השני
    return games[bot.__name__]["turn"]


def play(bot):
    # בדיקה ידנית: הבוט כותב, ואתם מקלידים את התשובות של הצד השני
    print(bot.TEAM_NAME + " - Turing Test Bot")
    message = ""
    if bot.STARTS_FIRST:
        message = respond(bot, "")
        print("Bot: " + message)
    for i in range(MAX_TURNS + 1):
        if not is_guess(message):
            their_message = input("Other side: ")
            message = respond(bot, their_message)
            print("Bot: " + message)
    print("Game over after " + str(turns(bot)) + " turns.")


if __name__ == "__main__": # רק כשמריצים את הקובץ הזה ישירות
    import turing_bot # הבוט שלכם (מייבאים כאן, כי turing_bot מייבא את הכלים מהקובץ הזה)
    play(turing_bot)