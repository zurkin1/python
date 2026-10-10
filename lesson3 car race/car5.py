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
COLORS = ["red", "blue", "yellow", "purple", "orange", "pink"]

# ---------------------------------------------------
# צורת מכונית - קוד מוכן, לא חייבים להבין אותו 🙂
# ---------------------------------------------------
def car_shape(color):
    name = "car_" + color
    if name not in screen.getshapes():
        car = turtle.Shape("compound")
        for x in [-23, 17]: # גלגלים
            for y in [-26, 14]:
                car.addcomponent(((x, y), (x + 6, y), (x + 6, y + 12), (x, y + 12)), "black")
        car.addcomponent(((-18, -32), (18, -32), (18, 32), (-18, 32)), color, "black") # גוף
        car.addcomponent(((-14, 6), (14, 6), (11, 18), (-11, 18)), "lightblue", "black") # שמשה קדמית
        car.addcomponent(((-13, -24), (13, -24), (11, -16), (-11, -16)), "lightblue", "black") # שמשה אחורית
        screen.register_shape(name, car)
    return name

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

def make_car(color, x, y, heading):
    car = turtle.Turtle()
    car.shape(car_shape(color))
    car.penup()
    car.setheading(heading) # 90 = למעלה, 270 = למטה
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
player = make_car("red", LANES[lane], -250, 90)

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
    enemy = make_car(random.choice(COLORS), random.choice(LANES), 450 + i * GAP, 270)
    enemies.append(enemy)

def reset_enemy(enemy):
    enemy.sety(enemy.ycor() + len(enemies) * GAP) # חוזרת למעלה, אחרי כל האחרות
    enemy.setx(random.choice(LANES))
    enemy.shape(car_shape(random.choice(COLORS)))

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
# 2. הוסיפו צבעים חדשים לרשימה COLORS.
# 3. הוסיפו נתיב רביעי לרשימה LANES (רמז: צריך גם כביש רחב יותר).
# 4. בונוס: הוסיפו 3 "חיים" - כל התנגשות מורידה חיים, ורק ב-0 המשחק נגמר.
#    (רמז: אחרי התנגשות - reset_enemy(enemy) כדי שהמכונית תיעלם)
# 5. בונוס: לחיצה על רווח מתחילה משחק חדש.
