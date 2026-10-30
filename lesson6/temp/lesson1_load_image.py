import pygame
from sys import exit

pygame.init()

WINDOW_SIZE=(800,600)

display=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('my pygame game')





#2 option = background
bg_image = pygame.image.load('res/bg.jpg')
bg_image = pygame.transform.scale(bg_image,(800,600))
display.blit(bg_image,(0,0))
ball_image = pygame.image.load('res/bouncing_ball.png')
display.blit(ball_image,(100,100))
pygame.display.update()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
