import pygame
from pygame.locals import *
import random
pygame.init()

width = 500
height = 500
screen_size = (width,height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('car race')

marker_width = 10
marker_height = 50

road = (100,0,300,height)
left_edge_marker = (95,0,marker_width,height)
right_edge_marker = (395,0,marker_width,height)
game_over = False
speed = 2
score = 0

left_lane = 150
center_lane = 250
right_lane = 350

lanes = [left_lane,center_lane,right_lane]

lane_marker_move_y = 0

class Vehicle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45/image.get_rect().height
        new_width = image.get_rect().width*image_scale
        new_height = image.get_rect().height*image_scale
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
class PlayerVehicle(Vehicle):
    def __init__(self,x,y):
        image = pygame.image.load("res/race/car.png")
        super().__init__(image,x,y)

player_x = 250
player_y = 400

player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x,player_y)
player_group.add(player)


image_filenames = ["pickup_truck.png","semi_trailer.png","taxi.png","van.png"]
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load("res/race/"+image_filename)
    vehicle_images.append(image)

vehicle_group = pygame.sprite.Group()

crash = pygame.image.load("res/race/crash.png")
crash_rect = crash.get_rect()

clock = pygame.time.Clock()
fps = 120


while game_over == False:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT and  player.rect.center[0] > left_lane:
                player.rect.x -= 100
            if event.key == K_RIGHT and  player.rect.center[0] < right_lane:
                player.rect.x += 100
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player,vehicle):
                    game_over = True
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left,(player.rect.center[1]+vehicle.rect.center[1])/2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

    screen.fill('lightgreen')
    pygame.draw.rect(screen,"gray",road)
    pygame.draw.rect(screen,"yellow",left_edge_marker)
    pygame.draw.rect(screen, "yellow", right_edge_marker)

    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height*2:
        lane_marker_move_y = 0
    for y in range(marker_height*-2 , height, marker_height*2):
        pygame.draw.rect(screen,"white", (left_lane+45, y+lane_marker_move_y, marker_width,marker_height))
        pygame.draw.rect(screen, "white", (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
    player_group.draw(screen)

    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False

        if add_vehicle:
            lane = random.choice(lanes)
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image,lane,height /-2)
            vehicle_group.add(vehicle)

    for vehicle in vehicle_group:
        vehicle.rect.y +=speed

        if vehicle.rect.top >= height:
            vehicle.kill()

    vehicle_group.draw(screen)

    if pygame.sprite.spritecollide(player,vehicle_group,True):
        game_over = True
        crash_rect.center = [player.rect.center[0],player.rect.top]
    if game_over:
        screen.blit(crash,crash_rect)
    pygame.display.update()