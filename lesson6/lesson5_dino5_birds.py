import pygame
from sys import exit
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1000,500))
bm_img = pygame.image.load("res/desert.jpg")
bm_img = pygame.transform.scale(bm_img,(1000,500))
dino_walking1_img = pygame.image.load("res/dino1.png")
dino_walking2_img = pygame.image.load("res/dino2.png")
dino_walking1_img = pygame.transform.scale(dino_walking1_img,(70,70))
dino_walking2_img = pygame.transform.scale(dino_walking2_img,(70,70))
current_walking = dino_walking1_img
dino_stopping_img = pygame.image.load("res/dino3.png")
plant1_img = pygame.image.load("res/plant1.png")
plant2_img = pygame.image.load("res/plant2.png")
current_plant = plant1_img
bird1_img = pygame.image.load("res/bird1.png")
bird2_img = pygame.image.load("res/bird2.png")
current_bird = bird1_img
bend_down_img = pygame.image.load("res/dino_down.png")
bend_down_img = pygame.transform.scale(bend_down_img,(70,70))
run = True
i=0
j=0
k=400
jump_i = 0
bend_i = 0
jumping_up_mode = False
jumping_down_mode = False
bend_down_mode = False
while run:
    clock.tick(300)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping_up_mode = True
            if event.key == pygame.K_DOWN:
                bend_down_mode = True
    #the background
    win.blit(bm_img,(-i,0))
    win.blit(bm_img,(1000-i,0))

    if i == 1000:
        i=0
    i=i+1

    if bend_down_mode == True:
       win.blit(bend_down_img,(100, 400))
       bend_i = bend_i + 1
       if (bend_i == 120):
           bend_i = 0
           bend_down_mode = False
    elif jumping_up_mode == True:
        win.blit(current_walking, (100, 400-jump_i))
        jump_i = jump_i + 1
        if jump_i == 200:
            jumping_up_mode = False
            jumping_down_mode = True
    elif jumping_down_mode == True:
        win.blit(current_walking, (100, 400-jump_i))
        jump_i = jump_i - 1
        if jump_i == 0:
            jumping_down_mode = False
    else:
        win.blit(current_walking, (100, 400))
        if current_walking == dino_walking1_img:
            current_walking = dino_walking2_img
        else:
            current_walking = dino_walking1_img
    #plants
    win.blit(current_plant,(1000-j,350))
    j = j+1
    if (j==1000):
        j=0
        if current_plant == plant1_img:
            current_plant = plant2_img
        else:
            current_plant = plant1_img
    #birds
    win.blit(current_bird, (1000 - k, 370))
    k = k + 1
    if (k == 1000):
        k = 0
    if current_bird == bird1_img:
        current_bird = bird2_img
    else:
        current_bird = bird1_img

    #check plant collision
    if 1000-j == 150 and jumping_up_mode == False and jumping_down_mode == False: #plant location
        run  = False
    # check bird collision
    if 1000 - k == 150 and bend_down_mode == False :  # bird location
        run = False
    pygame.display.update()