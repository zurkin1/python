import pygame
from sys import exit
import random
pygame.init()
WINDOW_SIZE=(800,600)
clock = pygame.time.Clock()
display=pygame.display.set_mode(WINDOW_SIZE,0,32)
bullets = []
game_on = True
bg_image = pygame.image.load('res/bg.jpg')
bg_image = pygame.transform.scale(bg_image,(800,600))
display.blit(bg_image,(0,0))
mario_image = pygame.image.load('res/mario.png')
display.blit(mario_image,(100,100))

pygame.display.update()

def check_collision():
    collision = False
    for bullet in bullets:
       #if abs(bullet - pygame.mouse.get_pos()[0]) <=10 and abs(bullet.y - pygame.mouse.get_pos()[1]) <=10:
       if bullet.collidepoint(pygame.mouse.get_pos()):
            print("collide xy")
            collision = True
    return collision

def shooting():
    for bullet in bullets:
        bullet_speed = random.randint(1,20)
        bullet.x = bullet.x+bullet_speed
        pygame.draw.rect(display,(0,0,128),(bullet.x,bullet.y,16,16))
        if bullet.x > 800:
            bullets.remove(bullet)
def add_bullet(location_ycor):
    rect = pygame.draw.rect(display, (0, 0, 128), (0, location_ycor, 16, 16))
    bullets.append(rect)

while game_on:
    #clock.tick(200)
    display.blit(bg_image, (0, 0))
    pos = pygame.mouse.get_pos()
    display.blit(mario_image, pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    location_ycor = random.randint(0,600)

    clock.tick(50)
    if len(bullets) <=10:
        add_bullet(location_ycor)
        clock.tick(50)
    shooting()
    if check_collision():
        game_on = False
    pygame.display.update()