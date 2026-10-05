import turtle
import random

sc = turtle.Screen()
sc.bgcolor('beige')
sc.setup(700, 700)


def prepare_game():
    board_image = 'board.gif'
    board.pu()
    board.back(100)
    board.shape(board_image)
    turtle_red.shape('turtle')
    turtle_red.color("red")
    turtle_red.shapesize(4)
    turtle_red.pu()
    turtle_red.goto(300, 300)

    turtle_blue.shape('turtle')
    turtle_blue.color("blue")
    turtle_blue.shapesize(4)
    turtle_blue.pu()
    turtle_blue.goto(300, 220)
    player_red.shape('turtle')
    player_red.shapesize(5)
    player_red.color("red")
    player_red.pu()
    player_red.goto((-485, -296))

    player_blue.shape('turtle')
    player_blue.shapesize(5)
    player_blue.color("blue")
    player_blue.pu()
    player_blue.goto((-500, -296))


def move_red(x,y):
    print("on prnt red")
    global player_red_location
    dice=random.randint(1,6)
    player_red_location = player_red_location + dice
    player_red.goto(locations_list[player_red_location])

def move_blue(x,y):
    print("on prnt red")
    global player_blue_location
    dice=random.randint(1,6)
    player_blue_location = player_blue_location + dice
    player_blue.goto(locations_list[player_blue_location])

sc.register_shape('board.gif')

locations_list = [(-485, -296), (-404, -297), (-326, -292), (-251, -291), (-186, -289), (-119, -291), (-57, -293),
                  (15, -286), (79, -290), (147, -290), (214, -287), (215, -220), (136, -223), (74, -220), (13, -223),
                  (-53, -220), (-119, -224), (-186, -223), (-255, -223), (-325, -225), (-402, -226), (-396, -150),
                  (-325, -156), (-257, -156), (-188, -157), (-116, -152), (-54, -154), (15, -153), (77, -154),
                  (141, -151), (215, -153), (213, -89), (140, -90), (75, -90), (13, -88), (-51, -90), (-119, -87),
                  (-184, -83), (-249, -86), (-321, -83), (-388, -85), (-388, -19), (-321, -21), (-254, -21),
                  (-182, -20), (-126, -19), (-51, -20), (14, -23), (78, -24), (136, -18), (208, -21), (211, 35),
                  (137, 39), (74, 45), (11, 43), (-52, 45), (-116, 47), (-182, 46), (-247, 47), (-320, 47), (-384, 53),
                  (-386, 116), (-321, 113), (-253, 112), (-185, 114), (-119, 109), (-48, 110), (12, 107), (82, 106),
                  (134, 110), (203, 107), (202, 168), (137, 174), (69, 172), (14, 173), (-54, 176), (-116, 177),
                  (-183, 178), (-247, 181), (-315, 178), (-388, 179), (-380, 250), (-304, 242), (-249, 241),
                  (-185, 239), (-122, 237), (-50, 239), (8, 233), (73, 234), (137, 230), (189, 233), (199, 292),
                  (129, 294), (71, 296), (9, 295), (-54, 302), (-127, 305), (-178, 302), (-246, 302), (-308, 309),
                  (-382, 316)]
ladder_list = [[1, 38], [4, 14], [9, 31], [28, 84], [21, 42], [71, 91], [80, 100], [51, 67]]
snake_list = [[17, 7], [64, 60], [62, 19], [87, 24], [93, 73], [98, 79], [100, 80], [95, 75]]

board = turtle.Turtle()
turtle_red = turtle.Turtle()
turtle_blue = turtle.Turtle()
player_red = turtle.Turtle()
player_blue = turtle.Turtle()
player_red_location=0
player_blue_location=0

prepare_game()
turtle_red.onclick(move_red)
turtle_blue.onclick(move_blue)
turtle.mainloop()