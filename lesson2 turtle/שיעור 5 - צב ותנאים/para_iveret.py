import turtle
import random

# הגדרת מסך המשחק
screen = turtle.Screen()
screen.setup(width=700, height=500)
screen.bgcolor("#0f172a")
screen.title("משחק בחירת דרך - לימוד תנאי if")

# יצירת הצב (השחקן)
player = turtle.Turtle()
player.shape("turtle")
player.color("#38bdf8")
player.pensize(3)
player.speed(3)


# פונקציה לכתיבת כותרות והודעות מעוצבות
def show_message(text, y_pos, color="#f8fafc", size=14):
    player.penup()
    player.goto(0, y_pos)
    player.color(color)
    player.write(text, align="center", font=("Arial", size, "bold"))


# הצגת כותרת המשחק
show_message("ברוכים הבאים למשחק בחירת הדרכים!", 200, "#a855f7", 18)
show_message("הצב עומד מול צומת דרכים. איזה צבע תבחרו?", 160, "#94a3b8", 12)

# ציור שני שבילים (ימין ושמאל)
# שביל שמאל (אדום)
player.penup()
player.goto(-100, 100)
player.pendown()
player.color("#ef4444")
player.goto(-200, 0)
player.penup()
player.goto(-200, -20)
player.write("שביל אדום (שמאל)", align="center", font=("Arial", 10, "normal"))

# שביל ימין (ירוק)
player.penup()
player.goto(100, 100)
player.pendown()
player.color("#22c55e")
player.goto(200, 0)
player.penup()
player.goto(200, -20)
player.write("שביל ירוק (ימין)", align="center", font=("Arial", 10, "normal"))

# החזרת הצב להתחלה
player.penup()
player.goto(0, 100)
player.color("#38bdf8")
player.setheading(270)  # פונה למטה

# שימוש בפקודת textinput כדי לקבל את בחירת השחקן
choice = screen.textinput("בחירת שחקן", "לאיזה שביל ללכת? הכנס 'אדום' או 'ירוק':")

# וידוא שהמשתמש לא ביטל את ההקלדה
if choice is None:
    choice = ""

# ניקוי הודעות קודמות ומיקום הצב למרכז ההחלטה
player.clear()
show_message(f"בחרת ב: {choice}", 200, "#fbbf24", 16)

# --- כאן מתבצע השימוש המרכזי בפקודת התנאי if ---
if choice == "אדום":
    # פעולות אם המשתמש בחר בשביל האדום
    player.penup()
    player.goto(0, 100)
    player.pendown()
    player.color("#ef4444")
    player.goto(-150, -50)

    show_message("הגעת לשביל האדום!", 50, "#ef4444", 14)
    show_message("ממצא: פגשת דרקון ידידותי! ניצחת במשחק! 🎉", 0, "#22c55e", 14)

elif choice == "ירוק":
    # פעולות אם המשתמש בחר בשביל הירוק
    player.penup()
    player.goto(0, 100)
    player.pendown()
    player.color("#22c55e")
    player.goto(150, -50)

    show_message("הגעת לשביל הירוק!", 50, "#22c55e", 14)
    show_message("ממצא: מצאת תיבת אוצר סודית! ניצחת בגדול! 🏆", 0, "#38bdf8", 14)

else:
    # פעולות ברירת מחדל אם הקלדה שגויה או ריקה (else)
    player.penup()
    player.goto(0, 50)
    player.color("#f43f5e")
    player.write("בחירה לא חוקית! הצב נשאר במקום ונבוך... 🐢❓", align="center", font=("Arial", 14, "bold"))

show_message("לחץ על המסך כדי לסגור את המשחק", -150, "#64748b", 10)
screen.exitonclick()