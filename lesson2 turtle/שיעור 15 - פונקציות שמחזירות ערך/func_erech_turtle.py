import turtle


def get_player_id(player):
    string_id = ""
    shape = player.shape()
    string_id = string_id+"shape: "+shape + "\n"
    distance_from_center = player.distance((0,0))
    string_id = string_id + "distance_from_center: " + str(distance_from_center)+"\n"
    pen_size = player.pensize()
    string_id = string_id + "pen_size: " + str(pen_size)+"\n"
    return string_id

player = turtle.Turtle()
player.shape('turtle')
player.goto(100,100)
print(player.pensize())
player_id = get_player_id(player)
print(player_id)


turtle.mainloop()