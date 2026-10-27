import pygame
from sys import exit
import time

def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(f'{current_time//1000}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time



clock = pygame.time.Clock()
pygame.init()
screen  = pygame.display.set_mode((800,500))
pygame.display.set_caption('Runner')


player_image = pygame.image.load('res/axe1.png')
player_image = pygame.transform.scale(player_image, (100, 100))
player_rect = player_image.get_rect(topleft = (80,450))

player_image2 = pygame.image.load('res/axe2.png')
player_image2 = pygame.transform.scale(player_image2, (100, 100))
player_rect2 = player_image2.get_rect(topleft = (80,350))

color_surface = pygame.Surface((800,500))
color_surface.fill('Beige')

snail_image = pygame.image.load('res/mario.png')
snail_image = pygame.transform.scale(snail_image, (50, 50))

snail_rect = snail_image.get_rect(bottomleft=(600,450))
test_font = pygame.font.Font(pygame.font.get_default_font(),50)

player_gravity = 0
snail_x_pos = 700
game_active = True
while True:
    if game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    if (player_rect.bottom == 450):
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    screen.blit(color_surface, (0, 0))
                    screen.blit(snail_image, snail_rect)
                    player_gravity += 1
                    player_rect2.y = player_rect.y
                    player_rect2.x = player_rect.x
                    screen.blit(player_image2, player_rect2)
                    pygame.display.update()
                    pygame.time.wait(100)

                if event.key == pygame.K_RIGHT:
                    screen.blit(color_surface, (0, 0))
                    screen.blit(snail_image, snail_rect)
                    player_rect.x = player_rect.x + 10
                    screen.blit(player_image, player_rect)
                    pygame.display.update()
                    pygame.time.wait(100)

                if event.key == pygame.K_LEFT:
                    screen.blit(color_surface, (0, 0))
                    screen.blit(snail_image, snail_rect)
                    player_rect.x = player_rect.x - 10
                    screen.blit(player_image, player_rect)
                    pygame.display.update()
                    pygame.time.wait(100)

        snail_x_pos = snail_x_pos - 1

        screen.blit(color_surface, (0, 0))
        screen.blit(snail_image, snail_rect)

        #screen.blit(text_surface, text_rect)
        snail_rect.x -=5
        if snail_rect.right <=0:
            snail_rect.left = 800
        if player_rect.x <= 0:
            player_rect.x = 0
        if player_rect.x >= 800:
            player_rect.x = 800
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 450:
            player_rect.bottom = 450
        screen.blit(player_image, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False


        score = display_score()
        pygame.display.update()
        clock.tick(30)
    else:
        color_surface.fill('Lightblue')
        score_surf = test_font.render(f'Your score: {score // 1000}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        screen.blit(color_surface, (0, 0))
        screen.blit(score_surf, score_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()