# -*- coding: utf-8 -*-
# ===================================================
# turtle6.py - הצב מקבל החלטות: משתנים + if + random 🎲
# ===================================================
# זוכרים משתנים ותנאי if מהשיעור הקודם? עכשיו הם עובדים עם הצב!

import turtle
import random # ספרייה להגרלת מספרים

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# --- שואלים את המשתמש ---
sides = screen.numinput("Question", "How many sides? (3-10)", default=5, minval=3, maxval=10) # חלון קלט
sides = int(sides) # הופכים למספר שלם

# --- תנאי: בוחרים צבע לפי מספר הצלעות ---
if sides == 3:
    t.color("red")
elif sides < 6:
    t.color("yellow")
else:
    t.color("cyan")

# --- ספירלה של מצולעים ---
for i in range(60):
    t.forward(i * 3)
    t.left(360 / sides + 1) # ה-+1 גורם לספירלה להסתובב

# --- 20 נקודות צבעוניות במקומות אקראיים ---
colors = ["red", "orange", "yellow", "lime", "magenta", "white"]
t.penup()
for i in range(20):
    x = random.randint(-300, 300) # מספר אקראי בין 300- ל-300
    y = random.randint(-250, 250)
    t.goto(x, y)
    if x > 0: # בצד ימין - נקודות גדולות
        t.dot(20, random.choice(colors))
    else: # בצד שמאל - נקודות קטנות
        t.dot(8, random.choice(colors))

t.hideturtle()
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. הוסיפו תנאי: אם sides == 4 - הצבע יהיה "lime".
# 2. שנו את range(60) ל-range(100). מה קרה?
# 3. בחרו צבע אקראי לכל קו בספירלה: t.color(random.choice(colors)) בתוך הלולאה.
# 4. בונוס: אם y > 0 הנקודה תהיה עגולה (dot), אחרת - הצב יחתים את עצמו (t.stamp()).
