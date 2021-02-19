import pygame
from settings import *
from player import Player
from map import world_map

def rgrid(x):
    return x // TILE * TILE


def Raycasting(screen,player):
    # mock
    world_size = 20

    
    for ray_n in range(N_RAYS):

        ray_angle = player.angle + ray_n * D_ANGLE - FOV/2
        
        x0 = player.x
        y0 = player.y

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        
        xv=yv=xh=yh= 99999999999

        # para baixo
        if sin_a > 0:
           yv = rgrid(y0)+TILE

           for _ in range(world_size):
                xv = x0 + (yv - y0)*cos_a/sin_a

                if (rgrid(xv),rgrid(yv)) in world_map:
                    #pygame.draw.circle(screen,GREEN,(int(xv),int(yv)),4)
                    break

                yv+=TILE

        # para cima
        if sin_a < 0:
            yv = rgrid(y0)

            for _ in range(world_size):
                xv = x0 + (yv - y0)*cos_a/sin_a
                if(rgrid(xv),rgrid(yv-TILE)) in world_map:
                    #pygame.draw.circle(screen,RED,(int(xv),int(yv)),4)
                    break
                yv-=TILE
        
        # para direita
        if cos_a > 0:
            xh = rgrid(x0)+TILE

            for _ in range(world_size):
                yh = y0 + (xh - x0)*sin_a/cos_a
                if(rgrid(xh),rgrid(yh)) in world_map:
                    #pygame.draw.circle(screen,(255,255,0),(int(xh),int(yh)),4)
                    break
                xh+=TILE

        # para esquerda
        if cos_a < 0:
            xh = rgrid(x0)

            for _ in range(world_size):
                yh = y0 + (xh - x0)*sin_a/cos_a
                if(rgrid(xh-TILE),rgrid(yh)) in world_map:
                    #pygame.draw.circle(screen,(0,255,255),(int(xh),int(yh)),4)
                    break
                xh-=TILE

        if (xh-x0)**2 + (yh-y0)**2  < (xv-x0)**2 + (yv-y0)**2:
            hit_point = (int(xh),int(yh))
        else:
            hit_point = (int(xv),int(yv))


        dist = math.sqrt((hit_point[0]-x0)**2+(hit_point[1]-y0)**2)

        # correcao olho de peixe
        z = math.cos(ray_angle - player.angle)

        proj_height = WALL_SCALE*PROJ_COEFF/(dist * z)
        c = 255/ (1+dist*dist*0.00001)
        color = (c,c/2,c/2)
        pygame.draw.rect(screen,color,(ray_n*SCALE,HEIGHT/2-proj_height//2,SCALE,proj_height))

'''
    pygame.draw.line(screen, RED, player.pos, (player.x + RENDER_DIST * math.cos(player.angle)
                                            , player.y + RENDER_DIST * math.sin(player.angle)))

    pygame.draw.line(screen, PURPLE, player.pos, (player.x + RENDER_DIST * math.cos(player.angle + FOV/2)
                                                , player.y + RENDER_DIST * math.sin(player.angle + FOV/2)))
    pygame.draw.line(screen, PURPLE, player.pos, (player.x + RENDER_DIST * math.cos(player.angle - FOV/2)
                                                , player.y + RENDER_DIST * math.sin(player.angle - FOV/2)))
'''


'''

def Raycasting(screen, player):
    x0,y0 = player.pos
    for ray_n in range(N_RAYS):
        ray_angle = player.angle + ray_n * D_ANGLE - FOV/2
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        for dist in range(20,RENDER_DIST,2):
            x = x0 + dist * cos_a
            y = y0 + dist * sin_a
            if(x//TILE*TILE,y//TILE*TILE) in world_map:
                dist*= math.cos(player.angle - ray_angle)
                proj_height = WALL_SCALE*PROJ_COEFF/dist
                c = 255/ (1+dist*dist*0.0001)
                color = (c,c/2,c/2)
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

    '''