import turtle
import random
import time

win = turtle.Screen()
win.setup(600, 800)
win.bgcolor('beige')
keep_playing = True
new_question = True
player_question = turtle.Turtle()
player_question.pu()
player_question.shape('blank')
player_question.goto(-20, 300)
right_answer_player = turtle.Turtle()
right_answer_player.pu()
right_answer_player.shape('blank')
wrong_answer1_player = turtle.Turtle()
wrong_answer1_player.pu()
wrong_answer1_player.shape('blank')
wrong_answer2_player = turtle.Turtle()
wrong_answer2_player.pu()
wrong_answer2_player.shape('blank')



while keep_playing:
    if new_question:
        right_answer_player.clear()
        wrong_answer1_player.clear()
        wrong_answer2_player.clear()
        player_question.clear()
        num1 = random.randint(1, 30)
        num2 = random.randint(10, 30)
        right_answer = num1 * num2
        wrong_answer1 = random.randint(right_answer - 20, right_answer + 20)
        wrong_answer2 = random.randint(right_answer - 20, right_answer + 20)
        player_question.write(str(num1) + "*" + str(num2), font=("arial", 28, "normal"))
        new_question = False


turtle.mainloop()

