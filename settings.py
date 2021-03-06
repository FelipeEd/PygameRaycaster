import  math

# game settings
WIDTH = 1200
HEIGHT = 800

FPS = 120
TILE = 100
FOV = 80 * math.pi / 180
MINI_SCALE = 1/4


# player settings
player_pos = (WIDTH//2,HEIGHT//2)
player_angle = 0
player_speed = 4
player_size = 5

# ray caster
N_RAYS = 120
D_ANGLE = FOV / N_RAYS
RENDER_DIST = 800
DIST = N_RAYS/(2*math.tan(FOV/2))
PROJ_COEFF = DIST * TILE
SCALE = WIDTH/ N_RAYS
WALL_SCALE = 5

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (0,0,255)
DARKGRAY = (10,10,10)
PURPLE = (120,0,120)
GROUND = (125, 159, 0)
SKY = (159, 185, 206)