import pygame
from settings import *
from player import Player
from map import world_map

def Raycasting(screen,player):
    x0,y0 = player.pos
    for ray_n in range(N_RAYS):
        ray_angle = player.angle + ray_n * D_ANGLE - FOV/2
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        for dist in range(1,RENDER_DIST,3):
            x = x0 + dist * cos_a
            y = y0 + dist * sin_a
            if(x//TILE*TILE,y//TILE*TILE) in world_map:
                dist*= math.cos(player.angle - ray_angle)
                proj_height = 3*PROJ_COEFF/dist
                c = 255/ (1+dist*dist*0.0001)
                color = (c,c//2,c)
                pygame.draw.rect(screen,color,(ray_n*SCALE,HEIGHT/2-proj_height//2,SCALE,proj_height))
                break
        #pygame.draw.line(screen, DARKGRAY, player.pos, (x,y), 2 )


    # Guide lines
    #pygame.draw.line(screen, RED, player.pos, (player.x + RENDER_DIST * math.cos(player.angle)
    #                                           , player.y + RENDER_DIST * math.sin(player.angle)))
    #pygame.draw.line(screen, PURPLE, player.pos, (player.x + RENDER_DIST * math.cos(player.angle + FOV/2)
    #                                              , player.y + RENDER_DIST * math.sin(player.angle + FOV/2)))
    #pygame.draw.line(screen, PURPLE, player.pos, (player.x + RENDER_DIST * math.cos(player.angle - FOV/2)
    #                                              , player.y + RENDER_DIST * math.sin(player.angle - FOV/2)))