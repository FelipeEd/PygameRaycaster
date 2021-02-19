from settings import  *

text_map = [
    'XXXXXXXXXXXX',
    'X..........X',
    'X.......X..X',
    'X........X.X',
    'X.........XX',
    'X....X.....X',
    'X....X.....X',
    'XXXXXXXX.XXX'
]

map_dimx = len(text_map)
map_dimy = len(text_map[0])

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'X':
            world_map.add((i * TILE, j * TILE))
