import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
KEY_WIDTH = SCREEN_WIDTH // 88  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("88-Key Piano")


key_colors = [WHITE, BLACK] * 44  

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for i, color in enumerate(key_colors):
        key_rect = pygame.Rect(i * KEY_WIDTH, 0, KEY_WIDTH, SCREEN_HEIGHT)
        pygame.draw.rect(screen, color, key_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
