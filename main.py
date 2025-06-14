# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set up time clock
    clock = pygame.time.Clock()
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
        player.update(dt)
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # pauses screen update
        dt = (clock.tick(60) / 1000)

    pygame.quit()

if __name__ == "__main__":
    main()

    


