# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set up time clock
    clock = pygame.time.Clock()
 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    # instance of AAsteroidField needed to be after .containers or get error
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    # instance of Player after containers or player ship not visible
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    dt = 0

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill("black")
        updatable.update(dt)

        
        for thing in drawable:
            thing.draw(screen)

        # Update the display
        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()

        # pauses screen update
        dt = (clock.tick(60) / 1000)

    pygame.quit()

if __name__ == "__main__":
    main()

    


