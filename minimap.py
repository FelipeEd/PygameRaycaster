import pygame
from settings import *
from map import world_map, map_dimx, map_dimy


def drawMinimap(screen, player, map, size_in_tiles):
    fac = 1 / max(map_dimx,map_dimy) * size_in_tiles

    p_x = (player.x) * fac
    p_y = (player.y) * fac
    pygame.draw.rect(screen, DARKGRAY, (0,0,TILE*size_in_tiles,TILE*size_in_tiles))

    for x, y in world_map:
        new_x = x * fac
        new_y = y * fac
        new_tile = TILE * fac

        pygame.draw.rect(screen, PURPLE, (new_x, new_y, new_tile, new_tile), 5)

    pygame.draw.circle(screen , GREEN, (int(p_x), int(p_y)), 7)