import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteriod = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriod, updatable, drawable)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    character = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asts in asteriod:
            if asts.collision(character):
                running = False
        pygame.display.flip()
        dt = clock.tick(60)/1000

main()