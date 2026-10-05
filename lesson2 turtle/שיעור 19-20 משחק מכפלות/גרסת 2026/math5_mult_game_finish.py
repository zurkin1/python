import turtle
import random
import time

win = turtle.Screen()
win.setup(600,800)
win.bgcolor('beige')
keep_playing = True
new_question = True
player_question = turtle.Turtle()
player_question.pu()
player_question.shape('blank')
player_question.goto(-20,300)
right_answer_player = turtle.Turtle()
right_answer_player.pu()
right_answer_player.shape('blank')
wrong_answer1_player = turtle.Turtle()
wrong_answer1_player.pu()
wrong_answer1_player.shape('blank')
wrong_answer2_player = turtle.Turtle()
wrong_answer2_player.pu()
wrong_answer2_player.shape('blank')

def finish_game():
    player_question.clear()
    player_question.goto(-100,300)
    player_question.write("WRONG!", font = ("Arial",30,"normal"))

def create_answers():
    right_ans = random.randint(1,4)
    if right_ans == 1:
        right_answer_player.goto(-60, 250)
        right_answer_player.write(right_answer, font=("arial", 18, "normal"))
        wrong_answer1_player.goto(0, 250)
        wrong_answer1_player.write(wrong_answer1, font=("arial", 18, "normal"))
        wrong_answer2_player.goto(60, 250)
        wrong_answer2_player.write(wrong_answer2, font=("arial", 18, "normal"))
    elif right_ans == 2:
        right_answer_player.goto(0, 250)
        right_answer_player.write(right_answer, font=("arial", 18, "normal"))
        wrong_answer1_player.goto(-60, 250)
        wrong_answer1_player.write(wrong_answer1, font=("arial", 18, "normal"))
        wrong_answer2_player.goto(60, 250)
        wrong_answer2_player.write(wrong_answer2, font=("arial", 18, "normal"))
    else:
        right_answer_player.goto(60, 250)
        right_answer_player.write(right_answer, font=("arial", 18, "normal"))
        wrong_answer1_player.goto(0, 250)
        wrong_answer1_player.write(wrong_answer1, font=("arial", 18, "normal"))
        wrong_answer2_player.goto(-60, 250)
        wrong_answer2_player.write(wrong_answer2, font=("arial", 18, "normal"))


def click_on_ans(x,y):
    global new_question
    global keep_playing
    if right_answer_player.xcor()+60>x>right_answer_player.xcor() and right_answer_player.ycor()+40>y>right_answer_player.ycor():
        new_question = True
    else:
        keep_playing = False
        finish_game()
def move_down(player, answer):
    time.sleep(0.1)
    yc = player.ycor()
    yc = yc - 20
    player.clear()
    player.goto(player.xcor(), yc)
    player.write(answer,font = ("arial", 18, "normal"))

win.onclick(click_on_ans)

while keep_playing:
    if new_question:
        right_answer_player.clear()
        wrong_answer1_player.clear()
        wrong_answer2_player.clear()
        player_question.clear()
        num1 = random.randint(1, 30)
        num2 = random.randint(10, 30)
        right_answer = num1 * num2
        wrong_answer1 = random.randint(right_answer - 20 ,right_answer + 20)
        wrong_answer2 = random.randint(right_answer - 20 ,right_answer + 20)
        player_question.write(str(num1)+"*"+str(num2), font = ("arial", 28, "normal"))
        create_answers()
        new_question = False
    move_down(right_answer_player, right_answer)
    move_down(wrong_answer1_player, wrong_answer1)
    move_down(wrong_answer2_player, wrong_answer2)


turtle.mainloop()

