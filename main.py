import pygame
from settings import *
from player import Player
import math
from map import world_map
from raycasting import  Raycasting

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.move()
    screen.fill(BLACK)
    pygame.draw.rect(screen,SKY,(0,0,WIDTH,HEIGHT//2))
    pygame.draw.rect(screen, GROUND, (0, HEIGHT//2, WIDTH, HEIGHT // 2))
    #pygame.draw.circle(screen,RED,(int(player.x),int(player.y)),10)
    Raycasting(screen,player)

    #for x, y in world_map:
    #    pygame.draw.rect(screen,BLUE,(x,y,TILE,TILE),2)

    pygame.display.flip()
    clock.tick(FPS)