import pygame
from settings import *
import math
from map import world_map


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.size = player_size

    @property
    def pos(self):
      return (self.x, self.y)

    def checkWall(self):
        
        return (self.x//TILE*TILE, self.y//TILE*TILE) in world_map

    def move(self):
        keys = pygame.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        old_x = self.x
        old_y = self.y
        # Somando as projeções em cada eixo para andar pra frente e traz
        # Pegando o vetor de cordenadas trocadas e com sinal oposto para andar
        # Perpendicular

        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y -= player_speed * cos_a
        if keys[pygame.K_s]:
            self.x -= player_speed * cos_a
            self.y -= player_speed * sin_a
        if keys[pygame.K_d]:
            self.x -= player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.1
        if keys[pygame.K_RIGHT]:
            self.angle += 0.1

        if self.checkWall():
            print("PAREDE")
            self.x = old_x
            self.y = old_y

        preci = 100
        # truncamento de posição
        self.x = int(self.x * preci)/preci
        self.y = int(self.y * preci)/preci

        self.angle = int(self.angle % (2*math.pi) *preci)/preci


