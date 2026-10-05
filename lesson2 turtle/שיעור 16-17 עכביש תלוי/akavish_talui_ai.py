import turtle
import random
from google import genai

client = genai.Client(api_key="AIzaSyDN8FNkomfKJyzNVDmocknDqaBfVaz1Ymg")

sc = turtle.Screen()
sc.bgcolor('beige')
sc.setup(800, 800)


def draw_spider():
    spider = turtle.Turtle()
    spider.speed(0)
    spider.shape('blank')
    spider.pensize(4)
    spider.pu()
    spider.goto(-200, 200)
    spider.pd()
    spider.setheading(-45)

    spider.goto(-250, 160)
    spider.pd()
    spider.fillcolor("black")
    spider.begin_fill()
    for _ in range(2):
        spider.circle(110, 90)  # רבע מעגל ראשון
        spider.circle(40, 90)  # רבע מעגל שני
    spider.end_fill()
    spider.pu()
    spider.goto(-150, 200)
    spider.pd()
    spider.fillcolor("white")
    spider.begin_fill()
    for _ in range(2):
        spider.circle(20, 90)  # רבע מעגל ראשון
        spider.circle(10, 90)  # רבע מעגל שני
    spider.end_fill()
    spider.pu()
    spider.goto(-230, 200)
    spider.pd()
    spider.fillcolor("white")
    spider.begin_fill()
    for _ in range(2):
        spider.circle(20, 90)  # רבע מעגל ראשון
        spider.circle(10, 90)  # רבע מעגל שני
    spider.end_fill()
    spider.setheading(0)

    spider.color("white")
    spider.pu()
    spider.goto(-210, 160)
    spider.pd()
    spider.forward(70)
    spider.color("black")
    spider.pu()
    spider.goto(-240, 225)
    spider.pd()
    spider.setheading(120)
    spider.forward(50)
    spider.lt(90)
    spider.forward(50)
    spider.pu()
    spider.goto(-260, 200)
    spider.pd()
    spider.setheading(150)
    spider.forward(50)
    spider.lt(90)
    spider.forward(50)
    spider.pu()
    spider.goto(-250, 155)
    spider.pd()
    spider.setheading(170)
    spider.forward(50)
    spider.lt(90)
    spider.forward(50)

    spider.pu()
    spider.goto(-108, 230)
    spider.pd()
    spider.setheading(20)
    spider.forward(50)
    spider.rt(90)
    spider.forward(50)
    spider.pu()
    spider.goto(-80, 200)
    spider.pd()
    spider.setheading(-10)
    spider.forward(50)
    spider.rt(90)
    spider.forward(50)
    spider.pu()
    spider.goto(-100, 150)
    spider.pd()
    spider.setheading(-40)
    spider.forward(50)
    spider.rt(90)
    spider.forward(50)
    spider.pu()
    spider.goto(-170, 250)
    spider.pd()
    spider.setheading(90)
    spider.speed(2)
    spider.forward(200)


turtle_list = []
color_list = ["red", "navy", "orange", "green", "pink", "brown", "blue"]


def end_game(status):
    global contPlaying
    line.goto(0, 0)
    message = "you " + status + "!"
    line.write(message, font=("arial", 28, "bold"))
    contPlaying = False


for i in range(7):
    t = turtle.Turtle()
    t.color(color_list[i])
    t.shape('turtle')
    t.pu()
    t.goto(random.randint(-300, 0), random.randint(-300, 0))
    turtle_list.append(t)


def letter_guessed(letter):
    guessed = False
    global guessed_letters_len
    for i in range(0, len(word)):
        if word[i] == letter and word_guessed_locations[i] == 0:
            word_guessed_locations[i] = 1
            guessed_letters_len = guessed_letters_len + 1
            guessed = True
    return guessed


def write_word():
    global word
    line.pu()
    line.goto(100, 100)
    line.clear()
    global word_guessed_locations
    for i in range(0, word_len):
        print(i)
        if word_guessed_locations[i] == 0:
            line.write("_", font=("courier", 38, "bold"))
            line.write("     ", font=("courier", 38, "bold"))
            line.forward(40)
        else:
            line.write(word[i] + '    ', font=("courier", 38, "bold"))
            line.forward(40)


def eat():
    global eating_stage
    if eating_stage == 6:
        end_game("Failed")
    tongue = turtle.Turtle()
    tongue.pu()
    tongue.shape('blank')
    tongue.goto(-175.0, 159.0)
    tongue.color("red")
    tongue.pensize(2)
    tongue.pd()
    tongue.goto(turtle_list[eating_stage].xcor(), turtle_list[eating_stage].ycor())
    turtle_list[eating_stage].hideturtle()
    eating_stage = eating_stage + 1
    tongue.clear()

word = client.models.generate_content(
    model="gemini-3.6-flash", contents="suggest one word for hanged man game, write only the word itself with small letters"
)
hanging_stage = 0
right_answers = 0
# the question
question = turtle.Turtle()
question.shape('blank')
question.pu()
question.goto(-200, 300)
question.write('guess the word', font=("Arial", 18, "normal"))
eating_stage = 0
contPlaying = True
# the lines
line = turtle.Turtle()
line.shape('blank')
line.pensize(4)
word_len = len(word.text)
guessed_letters_len = 0
word_guessed_locations = []
for _ in range (word_len):
    word_guessed_locations.append(0)
word = list(word.text)
print("after splitting:")
print(word)
write_word()
draw_spider()
while contPlaying:
    letter = turtle.textinput("enter letter", "enterletter")
    if letter_guessed(letter):
        write_word()
    else:
        eat()
    if guessed_letters_len == word_len:
        end_game("Succeeded")
turtle.mainloop()