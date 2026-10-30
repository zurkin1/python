import pygame
from sys import exit
pygame.font.init()
WIDTH, HEIGHT = 900,500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space game!")
FPS = 60
VEL = 5
BULLET_VEL=7
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2
MAX_BULLETS = 3

BORDER =  pygame.Rect(WIDTH//2 -5, 0,10, HEIGHT)
HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WIN_FONT = pygame.font.SysFont('comicsans',100)
RED_SPACESHIP_IMAGE = pygame.image.load('res/space/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

YELLOW_SPACESHIP_IMAGE = pygame.image.load('res/space/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
SPACE_IMAGE = pygame.image.load('res/space/space.png')
SPACE = pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    #WIN.fill("White")

    WIN.blit(SPACE,(0,0))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    pygame.draw.rect(WIN, "Black", BORDER)
    red_health_text = HEALTH_FONT.render("Health: "+str(red_health),1,'white')
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, 'white')
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,"Red",bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,"Yellow",bullet)
    pygame.display.update()

def handle_yellow_movement(keys_pressed, yellow):
    if (keys_pressed[pygame.K_a] and yellow.x - VEL > 0):
        yellow.x -= VEL
    if (keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x) :
        yellow.x += VEL
    if (keys_pressed[pygame.K_w] and yellow.y - VEL > 0):
        yellow.y -= VEL
    if (keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15):
        yellow.y += VEL

def handle_red_movement(keys_pressed, red):
    if (keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width):
        red.x -= VEL
    if (keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH):
        red.x += VEL
    if (keys_pressed[pygame.K_UP] and red.y - VEL > 0):
        red.y -= VEL
    if (keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT -15):
        red.y += VEL

def draw_winner(win_text):
    draw_text = WIN_FONT.render(win_text,1,'white')
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    exit()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
clock = pygame.time.Clock()
yellow_bullets = []
red_bullets = []
red_health = 10
yellow_health = 10

run  = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(yellow_bullets)< MAX_BULLETS:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.width//2,10,5)
                yellow_bullets.append(bullet)
            if event.key == pygame.K_RCTRL and len(red_bullets)< MAX_BULLETS:
                bullet = pygame.Rect(red.x , red.y + red.width//2,10,5)
                red_bullets.append(bullet)

        if event.type == RED_HIT:
            red_health -= 1
        if event.type == YELLOW_HIT:
            yellow_health -=1

    win_text = ""
    if red_health <= 0:
        win_text = "YELLOW WON!"
    if yellow_health <= 0:
        win_text = "RED WON!"
    if win_text != "":
        draw_winner(win_text)
    keys_pressed = pygame.key.get_pressed()
    handle_yellow_movement(keys_pressed,yellow)
    handle_red_movement(keys_pressed, red)
    handle_bullets(yellow_bullets,red_bullets,yellow,red)
    draw_window(red,yellow, red_bullets,yellow_bullets, red_health,yellow_health)

    #pygame.quit()
