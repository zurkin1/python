# -*- coding: utf-8 -*-
# ===================================================
# car5.py - המשחק המלא: הרבה מכוניות, ניקוד ומהירות 🏁🏆
# ===================================================
# כמה מכוניות באות מולכם - כולן שמורות ברשימה אחת: enemies
# כל מכונית שעוברת = נקודה, והמשחק נהיה מהיר יותר ויותר!
# חיצים ימינה/שמאלה = החלפת נתיב

import turtle
import random

screen = turtle.Screen()
screen.setup(500, 700)
screen.bgcolor("forestgreen")
screen.title("Car Race!")
screen.tracer(0) # מכבים ציור אוטומטי - אנחנו נעדכן את המסך בעצמנו

LANES = [-120, 0, 120] # רשימה: מיקום x של כל נתיב
ENEMIES = ["enemy_blue.gif", "enemy_yellow.gif", "enemy_purple.gif", "enemy_orange.gif", "enemy_pink.gif"]

# ---------------------------------------------------
# תמונות המכוניות - קבצי gif שנמצאים באותה תיקייה עם הקוד
# ---------------------------------------------------
screen.register_shape("player.gif") # המכונית שלנו (פונה למעלה)
for image in ENEMIES: # המכוניות שבאות מולנו (פונות למטה)
    screen.register_shape(image)

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

def draw_road():
    draw_rect(-180, -350, 360, 700, "dimgray") # הכביש
    draw_rect(-186, -350, 6, 700, "white") # שוליים משמאל
    draw_rect(180, -350, 6, 700, "white") # שוליים מימין

def make_car(image, x, y):
    car = turtle.Turtle()
    car.shape(image) # התמונה היא הצורה של הצב
    car.penup()
    car.goto(x, y)
    return car # מחזירים את המכונית החדשה

# ---------------------------------------------------
# הקווים המקווקווים - רשימה של צבים קטנים
# ---------------------------------------------------
lines = []
for x in [-60, 60]:
    for y in range(-360, 360, 80):
        line = turtle.Turtle()
        line.shape("square")
        line.color("white")
        line.shapesize(2, 0.3) # מלבן צר וארוך
        line.penup()
        line.goto(x, y)
        lines.append(line)

def move_lines():
    for line in lines:
        line.sety(line.ycor() - speed)
        if line.ycor() < -360:
            line.sety(line.ycor() + 720) # חוזר למעלה

# ---------------------------------------------------
# השחקן
# ---------------------------------------------------
draw_road()
lane = 1 # האינדקס של הנתיב ברשימה LANES (0, 1 או 2)
player = make_car("player.gif", LANES[lane], -250)

def move_left():
    global lane
    if lane > 0:
        lane = lane - 1
        player.setx(LANES[lane])

def move_right():
    global lane
    if lane < len(LANES) - 1:
        lane = lane + 1
        player.setx(LANES[lane])

# ---------------------------------------------------
# המכוניות שבאות מולנו - רשימה!
# ---------------------------------------------------
GAP = 300 # מרחק בין מכונית למכונית
enemies = []
for i in range(3):
    enemy = make_car(random.choice(ENEMIES), random.choice(LANES), 450 + i * GAP)
    enemies.append(enemy)

def reset_enemy(enemy):
    enemy.sety(enemy.ycor() + len(enemies) * GAP) # חוזרת למעלה, אחרי כל האחרות
    enemy.setx(random.choice(LANES))
    enemy.shape(random.choice(ENEMIES))

def crashed(car1, car2): # מחזירה True אם המכוניות נוגעות
    close_x = abs(car1.xcor() - car2.xcor()) < 36
    close_y = abs(car1.ycor() - car2.ycor()) < 64
    return close_x and close_y

# ---------------------------------------------------
# ניקוד
# ---------------------------------------------------
score = 0
speed = 6
game_over = False

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("yellow")

def show_score():
    writer.clear()
    writer.goto(0, 300)
    writer.write("Score: " + str(score), align="center", font=("Arial", 22, "bold"))

# ---------------------------------------------------
# לולאת המשחק - רצה שוב ושוב, 50 פעמים בשנייה
# ---------------------------------------------------
def game_loop():
    global score, speed, game_over
    move_lines()
    for enemy in enemies:
        enemy.sety(enemy.ycor() - speed)
        if enemy.ycor() < -400: # יצאה מהמסך למטה
            reset_enemy(enemy)
            score = score + 1
            speed = speed + 0.3 # כל נקודה - קצת יותר מהר!
            show_score()
        if crashed(player, enemy):
            game_over = True

    screen.update() # מציירים את המסך מחדש
    if game_over:
        writer.goto(0, 20)
        writer.write("CRASH!", align="center", font=("Arial", 40, "bold"))
        writer.goto(0, -20)
        writer.write("Score: " + str(score), align="center", font=("Arial", 24, "bold"))
        screen.update()
    else:
        screen.ontimer(game_loop, 20) # עוד 20 אלפיות שנייה - שוב!

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

show_score()
game_loop()
turtle.done()

# ===================================================
# 🏆 אתגרים:
# ===================================================
# 1. שנו את מספר המכוניות ל-4 (בלולאה range). מה קורה?
# 2. ציירו מכונית משלכם בצייר (gif, בערך 40x70), הוסיפו אותה לרשימה ENEMIES.
# 3. הוסיפו נתיב רביעי לרשימה LANES (רמז: צריך גם כביש רחב יותר).
# 4. בונוס: הוסיפו 3 "חיים" - כל התנגשות מורידה חיים, ורק ב-0 המשחק נגמר.
#    (רמז: אחרי התנגשות - reset_enemy(enemy) כדי שהמכונית תיעלם)
# 5. בונוס: לחיצה על רווח מתחילה משחק חדש.
