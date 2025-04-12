# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from circleshape import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable) 

    asteroid_field = AsteroidField()

    pygame.init()
    pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0
    player_shot_timer = PLAYER_SHOOT_COOLDOWN
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot) == True:
                    asteroid.split()
            if asteroid.check_collision(player) == True:
                print('Game over')
                sys.exit()
        screen.fill('black')
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60)/1000

if __name__ == "__main__":
    main()