# -*- coding: utf-8 -*-
# ===================================================
# turing_bot_sol.py - פתרון לדוגמה (למורה בלבד!) 🕵️
# ===================================================
# אסטרטגיה:
#   1. מתחזה: אישיות מפורטת ועקבית של נער בן 13, עם סגנון כתיבה אנושי
#   2. מלכודת: שאלת חשבון קשה - בן אדם לא יענה מהר תשובה מדויקת, Gemini כן
#   3. בדיקות מהירות בלי Gemini: הצד השני מעתיק אותנו, או עונה את התשובה המדויקת למלכודת
#   4. בלש: קריאה נפרדת ל-Gemini שמנתחת את השיחה ומחזירה פסק דין + ביטחון (0-100)
#   5. ניחוש רק כשהבלש בטוח מספיק. ככל שעוברים תורות - מספיק פחות ביטחון
#   6. כותב: קריאה שנייה ל-Gemini שעונה כמו נער, ושואלת שאלה לפי ההצעה של הבלש

from bot_tools import ask_gemini, history_text, MAX_TURNS


# ===================================================
# הגדרות
# ===================================================
TEAM_NAME = "Sherlock"
STARTS_FIRST = True

TRAP_QUESTION = "כמה זה 389 כפול 47? בלי מחשבון חחח"
TRAP_ANSWER = "18283" # 389 * 47

# ===================================================
# 1. הוראות המערכת: המתחזה (כותב את ההודעות שלנו)
# ===================================================
SYSTEM_PROMPT = """
אתה עומר, בן 13 מרמת גן, כיתה ח'. אוהד מכבי תל אביב, משחק ברול סטארס, יש לך אחות קטנה מעצבנת וכלב בשם בוני.
אתה מתכתב עם מישהו ומנסה לגלות אם הוא בן אדם או בוט, אבל אתה כותב כמו נער אמיתי:
- הודעות קצרות (בדרך כלל 5-15 מילים), עד 25 מילים לכל היותר. בעברית.
- סלנג, לפעמים "חחח", לפעמים שגיאת כתיב קטנה, בלי פיסוק מושלם. לפעמים בלי סימני שאלה.
- אתה לא יודע הכול: על שאלות קשות (חשבון, מדע, היסטוריה) תענה "אין לי מושג" או תנחש בערך.
- אל תתחיל כל הודעה באותה מילה, ואל תסיים כל הודעה בשאלה.
- אף פעם אל תגיד שאתה בוט, ואל תסביר את עצמך יותר מדי.
בשיחה: Me = אתה, Other = הצד השני.
"""

# ===================================================
# 2. הבלש: מנתח את השיחה (קריאה נפרדת ל-Gemini)
# ===================================================
DETECTIVE_PROMPT = """
You are an expert judge in a Turing test. Read the chat (Me = us, Other = the one we judge).
Decide if Other is a HUMAN teenager or a BOT (a language model pretending to be human).
Signs of a BOT: perfect grammar and punctuation, polished or long sentences, too much knowledge,
exact answers to hard math, always ending with a question, repeating the same opening word,
answering every part of every question, overly friendly or balanced tone, copying our style or our message.
Signs of a HUMAN: typos, very short or lazy answers, "idk", ignoring questions, changing the subject,
small inconsistencies, real-time details, rude or random replies.
Reply in exactly this format:
VERDICT CONFIDENCE ASK
VERDICT = BOT, HUMAN or UNSURE. CONFIDENCE = a number 0-100. ASK = a short idea (in Hebrew) for our next question.
Example: BOT 80 תשאל אותו מה השעה אצלו עכשיו
"""

OPENING_LINES = [
    "היי מה קורה? מה אכלת היום בבוקר",
]


def last_other(history):
    # ההודעה האחרונה של הצד השני
    for line in reversed(history):
        if line.startswith("Other: "):
            return line[len("Other: "):]
    return ""


def quick_check(history):
    # בדיקות מהירות בלי Gemini. מחזירה ניחוש, או "" אם אין ממצא
    their = last_other(history)
    if TRAP_ANSWER in their.replace(",", ""): # ענה בדיוק על שאלת החשבון הקשה
        return "GUESS: BOT"
    for line in history:
        if line.startswith("Me: ") and line[len("Me: "):] == their: # העתיק הודעה שלנו מילה במילה
            return "GUESS: BOT"
    return ""


def detective(history):
    # מחזירה [פסק דין, ביטחון, רעיון לשאלה]
    reply = ask_gemini(DETECTIVE_PROMPT, history_text(history), temperature=0)
    words = reply.split()
    verdict = "UNSURE"
    confidence = 0
    ask = ""
    if len(words) >= 2 and words[0].upper() in ("BOT", "HUMAN", "UNSURE") and words[1].isdigit():
        verdict = words[0].upper()
        confidence = int(words[1])
        ask = " ".join(words[2:])
    print("[detective]", verdict, confidence, ask) # כדי שנראה מה הבלש חושב
    return [verdict, confidence, ask]


def needed_confidence(turn):
    # כמה ביטחון צריך כדי לנחש: בהתחלה הרבה, ובהמשך פחות
    if turn <= 1:
        return 95
    if turn <= 3:
        return 85
    if turn <= 5:
        return 75
    return 65


def write_message(history, turn, sent, ask):
    prompt = "זו השיחה עד עכשיו:\n" + history_text(history) + "\n"
    prompt = prompt + "כתוב את ההודעה הבאה שלך (עומר). אם הצד השני שאל משהו - תענה לו קודם, כמו נער.\n"
    if sent == 1:
        prompt = prompt + "בהודעה הזו תשאל גם, בצורה טבעית: " + TRAP_QUESTION + "\n"
    elif ask != "":
        prompt = prompt + "אחר כך תשאל שאלה קצרה ברוח הזו: " + ask + "\n"
    prompt = prompt + "רק ההודעה עצמה, בלי הסברים."
    return ask_gemini(SYSTEM_PROMPT, prompt, temperature=0.9)


# ===================================================
# 3. המוח של הבוט
# ===================================================
def decide(history, turn, sent):
    # פתיחה קבועה - רק כשאנחנו פותחים
    if STARTS_FIRST and sent < len(OPENING_LINES):
        return OPENING_LINES[sent]

    # בדיקות מהירות
    found = quick_check(history)
    if found != "":
        return found

    # הבלש
    result = detective(history)
    verdict = result[0]
    confidence = result[1]
    ask = result[2]
    if verdict == "BOT" and confidence >= needed_confidence(turn):
        return "GUESS: BOT"
    # על "בן אדם" זהירים יותר: Gemini מתחזה טוב, וקל ליפול בפח
    if verdict == "HUMAN" and turn >= 4 and confidence >= needed_confidence(turn) + 10:
        return "GUESS: HUMAN"

    # תור אחרון - חייבים לנחש: לפי הבלש, ואם הוא לא בטוח - BOT (Gemini מתחזה טוב, אבל לא מושלם)
    if turn >= MAX_TURNS:
        if verdict == "HUMAN":
            return "GUESS: HUMAN"
        return "GUESS: BOT"

    return write_message(history, turn, sent, ask)