import random
import config
import map  # Importa el módulo map completo

#Andres Murcia:

class Entity:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, direction):
        dr, dc = direction
        new_row, new_col = self.row + dr, self.col + dc
        if 0 <= new_row < config.ROWS and 0 <= new_col < config.COLS and map.maze[new_row][new_col] == 0:
            self.row, self.col = new_row, new_col

    def get_pos(self):
        return self.row, self.col

    def draw(self, screen, color):
        from pygame.draw import circle
        x = self.col * config.TILE_SIZE + config.TILE_SIZE // 2
        y = self.row * config.TILE_SIZE + config.TILE_SIZE // 2
        circle(screen, color, (x, y), config.TILE_SIZE // 2 - 5)

class Ghost(Entity):
    def auto_move(self):
        from config import DIRECTIONS
        direction = random.choice(list(DIRECTIONS.values()))
        self.move(direction)