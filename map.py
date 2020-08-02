from settings import  *

text_map = [
    'XXXXXXXXXXXX',
    'X.......XX.X',
    'X..X...X...X',
    'X.....X....X',
    'X....X.....X',
    'X..XXXX....X',
    'X..........X',
    'XXXXXXXXXXXX'
]

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'X':
            world_map.add((i * TILE, j * TILE))
