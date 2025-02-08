import pygame
from constants import *
from player import Player


def main():
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    character = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        character.draw(screen)
        character.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000

main()