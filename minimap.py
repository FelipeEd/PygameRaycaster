import pygame
from settings import *
from map import world_map

def drawMinimap(screen, player, map):
    minimap = (0, HEIGHT - HEIGHT * MINI_SCALE, WIDTH * MINI_SCALE, HEIGHT)
    p_x = (player.x * MINI_SCALE)
    p_y = (player.y * MINI_SCALE) + HEIGHT - HEIGHT * MINI_SCALE
    pygame.draw.rect(screen, DARKGRAY, minimap)
    for x, y in world_map:
        new_x = (x * MINI_SCALE)
        new_y = (y * MINI_SCALE) + HEIGHT - HEIGHT * MINI_SCALE
        new_tile = TILE* MINI_SCALE
        pygame.draw.rect(screen, PURPLE, (new_x,new_y, new_tile,new_tile), 5)

    pygame.draw.circle(screen , GREEN, (int(p_x), int(p_y)), 7)