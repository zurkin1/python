import pygame
from sys import exit
pygame.init()

WINDOW_SIZE=(800,800)

screen=pygame.display.set_mode(WINDOW_SIZE,0,32)
pygame.display.set_caption('my pygame game')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()