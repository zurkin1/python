import pygame
from sys import exit

pygame.init()

WINDOW_SIZE=(800,800)

display=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('my pygame game')

surface1 = pygame.Surface((10,10))
surface1.fill((255,0,0)) # red
surface2 = pygame.Surface((20,20))
surface2.fill('Blue')
surface3 = pygame.Surface((30,30))
surface3.fill('Yellow')
surface4 = pygame.Surface((40,40))
surface4.fill('Green')

display.blit(surface1,(100,100))
display.blit(surface2,(200,200))
display.blit(surface3,(300,300))
display.blit(surface4,(400,400))
pygame.display.update()
while True:
    display.blit(surface1, (20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
