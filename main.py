import pygame
from settings import *
from player import Player
import math
from map import world_map
from raycasting import  Raycasting
from minimap import drawMinimap

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
font = pygame.font.SysFont("Arial", 18)


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.move()
    screen.fill(BLACK)
    pygame.draw.rect(screen,SKY,(0,0,WIDTH,HEIGHT//2))
    pygame.draw.rect(screen, GROUND, (0, HEIGHT//2, WIDTH, HEIGHT // 2))

    Raycasting(screen,player)

    drawMinimap(screen, player, world_map)
    screen.blit(update_fps(), (10, 0))


    pygame.display.flip()
    clock.tick(FPS)