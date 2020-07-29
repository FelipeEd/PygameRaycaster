import  math

# game settings
WIDTH = 1200
HEIGHT = 800
FPS = 60
TILE = 100
FOV = 60 * math.pi / 180


# player settings
player_pos = (WIDTH//2,HEIGHT//2)
player_angle = 0
player_speed = 5

# ray caster
N_RAYS = 120
D_ANGLE = FOV / N_RAYS
RENDER_DIST = 800
DIST = N_RAYS/(2*math.tan(FOV/2))
PROJ_COEFF = DIST * TILE
SCALE = WIDTH/ N_RAYS

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGRAY = (110,110,110)
PURPLE = (120,0,120)
GROUND = (59,50,50)
SKY = (20,20,200)