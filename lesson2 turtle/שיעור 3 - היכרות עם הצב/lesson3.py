import turtle


#הגדרת מסך

win = turtle.Screen()
win.bgcolor('lightgreen')
win.setup(500,500)
#הגדרת דמות
player1 = turtle.Turtle()

#מאפיינים של הדמות
player1.shape('turtle')
player1.color('red')
player1.pensize(2)
player1.speed(1)
#תנועה של הדמות


player1.goto(20,60)
player1.setpos(0,0)
player1.forward(50)
player1.backward(200)
player1.right(90)
player1.forward(100)
player1.left(90)
player1.forward(60)

#אפשר להגדיר עוד דמות
player2 = turtle.Turtle()

player2.shape('circle')
player2.color('yellow')
player2.pensize(3)
player2.speed(3)
player2.forward(150)

#עבודה עם משתנים

color = "pink"
player2.color(color)
pensize = 2
player2.pensize(pensize)
#פה כבר לא צריך "", כי אנחנו משתמשים במשתנה





#שהחלון לא ייסגר
turtle.mainloop()