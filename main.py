import pygame, sys
import config  # Importa config
from entities import Entity, Ghost
import map
import ui

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))  # Accede a WIDTH y HEIGHT a través de config
pygame.display.set_caption("Mini Pac-Man")
clock = pygame.time.Clock()

# Entidades y estado
pacman = Entity(1, 1)
ghost = Ghost(8, 8)
pellets = map.generate_pellets()
score = 0
game_over = False
start_screen = True

# Bucle principal
while True:
    if start_screen:
        screen.fill(config.BLACK)  # Accede a BLACK a través de config
        ui.draw_text(screen, "Presiona ESPACIO para comenzar", 30, 50, 170, config.WHITE)  # Accede a WHITE a través de config
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_screen = False

    elif game_over:
        screen.fill(config.BLACK)  # Accede a BLACK a través de config
        ui.draw_text(screen, "GAME OVER", 40, 130, 160, config.RED)  # Accede a RED a través de config
        ui.draw_text(screen, f"Puntaje: {score}", 30, 150, 210, config.GREEN)  # Accede a GREEN a través de config
        ui.draw_text(screen, "Presiona ESC para salir", 20, 110, 250, config.WHITE)  # Accede a WHITE a través de config
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit(); sys.exit()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in config.DIRECTIONS:  # Accede a DIRECTIONS a través de config
                    pacman.move(config.DIRECTIONS[event.key])  # Accede a DIRECTIONS a través de config

        # Comer punto
        if pacman.get_pos() in pellets:
            pellets.remove(pacman.get_pos())
            score += 10
            if not pellets:
                game_over = True

        # Mover fantasma
        ghost.auto_move()

        # Colisión con fantasma
        if pacman.get_pos() == ghost.get_pos():
            game_over = True

        # Dibujar escena
        screen.fill(config.BLACK)  # Accede a BLACK a través de config
        ui.draw_maze(screen)
        ui.draw_pellets(screen, pellets)
        pacman.draw(screen, config.YELLOW)  # Accede a YELLOW a través de config
        ghost.draw(screen, config.RED)  # Accede a RED a través de config
        ui.draw_text(screen, f"Puntos: {score}", 24, 10, 10, config.GREEN)  # Accede a GREEN a través de config
        pygame.display.flip()
        clock.tick(config.FPS)  # Accede a FPS a través de config