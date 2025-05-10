import random
from config import ROWS, COLS

# Mapa del laberinto
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1],
    [1,0,1,1,0,1,0,1,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,1,0,0,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

# Genera 30 puntos en posiciones válidas
def generate_pellets():
    pellets = set()
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == 0:
                pellets.add((r, c))
    return set(random.sample(list(pellets), 30))