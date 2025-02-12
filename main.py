import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
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
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriod, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    field = AsteroidField()
    character = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    img = pygame.image.load("/Users/ericdavoodi/repos/pythonrepos/asteroid/spaceback.jpeg")


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        screen.blit(img, (0, 0))
        for item in drawable:
            item.draw(screen)
        for asts in asteriod:
            if asts.collision(character):
                running = False
            for shot in shots:
                if asts.collision(shot):
                    asts.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000

main()