# -*- coding: utf-8 -*-
# ===================================================
# homework_ans.py - פתרון שיעורי הבית: 20 שאלות 🤔
# ===================================================
# אתם חושבים על משהו (אדם מפורסם, חיה, ספר, מקום...),
# ו-Gemini מנסה לגלות מה זה עם 20 שאלות של כן/לא לכל היותר.
# משתמשים בכלים מ-bot_tools.py (צריך שיהיה באותה תיקייה, עם המפתח).

from bot_tools import ask_gemini, history_text


MAX_QUESTIONS = 20

SYSTEM_PROMPT = """
אתה משחק "20 שאלות". המשתמש חשב על משהו: אדם מפורסם, חיה, ספר, מקום, חפץ או כל דבר אחר.
אתה צריך לגלות מה זה. בכל תור כתוב שאלה אחת בלבד, קצרה, שאפשר לענות עליה כן או לא. בעברית.
תתחיל משאלות כלליות (בן אדם? חיה? חפץ?) ותצמצם בהדרגה. אל תחזור על שאלות ששאלת כבר.
כשאתה די בטוח - כתוב רק: GUESS: והניחוש שלך. למשל: GUESS: פיל
כתוב רק את השאלה או את הניחוש, בלי הסברים.
"""

history = [] # כל השאלות והתשובות עד עכשיו
found = False # האם Gemini כבר גילה?

print("=== 20 שאלות ===")
print("תחשבו על משהו: אדם מפורסם, חיה, ספר, מקום...")
input("כשאתם מוכנים - לחצו Enter ")

for number in range(1, MAX_QUESTIONS + 1):
    if not found:
        prompt = "זו השיחה עד עכשיו:\n" + history_text(history) + "\n"
        prompt = prompt + "נשארו לך " + str(MAX_QUESTIONS - number + 1) + " שאלות. מה השאלה הבאה שלך?"
        if number == MAX_QUESTIONS:
            prompt = prompt + " זו השאלה האחרונה - אתה חייב לנחש: GUESS: ..."
        question = ask_gemini(SYSTEM_PROMPT, prompt, temperature=0.3)

        if question.upper().startswith("GUESS:"): # Gemini מנחש
            guess = question[len("GUESS:"):].strip()
            answer = input("שאלה " + str(number) + " - Gemini מנחש: " + guess + "! צדקתי? (כן/לא) ")
            history.append("ניחוש: " + guess + " - תשובה: " + answer)
            if answer.strip() == "כן":
                found = True
                print("🎉 Gemini גילה אחרי " + str(number) + " שאלות!")
        else: # שאלה רגילה
            answer = input("שאלה " + str(number) + ": " + question + " ")
            history.append("שאלה: " + question)
            history.append("תשובה: " + answer)

if not found:
    secret = input("Gemini לא הצליח לגלות... על מה חשבתם? ")
    print("כל הכבוד! " + secret + " ניצח את Gemini 😎")