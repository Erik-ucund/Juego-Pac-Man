import pygame
import config
import map  # Importa el módulo map

def draw_maze(screen):
    for r in range(len(map.maze)):
        for c in range(len(map.maze[0])):
            if map.maze[r][c] == 1:
                pygame.draw.rect(screen, config.BLUE, (c * config.TILE_SIZE, r * config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE))

def draw_pellets(screen, pellets):
    for r, c in pellets:
        pygame.draw.circle(screen, config.WHITE, (c * config.TILE_SIZE + config.TILE_SIZE//2, r * config.TILE_SIZE + config.TILE_SIZE//2), 5)

def draw_text(screen, text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))