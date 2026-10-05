import turtle
#להדפיס מספרים מ 1 עד 10
for i in range(1,11):
    print(i)

#להדפיס מספרים בקפיצות של 2
for i in range(2,101,2):
    print(i)

#תנאי בתוך לולאה
for i in range(2,101,2):
    if i != 50:
        print(i)

#לסכום מספרים מ 1 עד 100
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

#חישוב עצרת של 10
mult = 1
for i in range(1,11):
    mult = mult * i
print(mult)

# דמות שמתקדמת בלולאה
player = turtle.Turtle()
player.color('purple')
player.shape('turtle')
step_size = turtle.numinput("enter step size","enter step size" )
num_steps = turtle.numinput("enter num steps","enter num steps" )
for i in range(1, int(num_steps)):
    player.forward(step_size)

#ריבוע בלולאה

for i in range(1, 5):
    player.forward(100)
    player.right(90)
#משולש בלולאה
for i in range(1, 4):
    player.forward(100)
    player.right(120)
#משושה בלולאה
for i in range(1, 7):
    player.forward(100)
    player.right(60)


#פרח בלולאה
for i in range(1, 6):
    player.circle(100,180)
    player.right(108)

turtle.mainloop()