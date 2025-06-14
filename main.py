# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill(black)
    
        # Fill a rectangle with red
        #pygame.draw.rect(screen, red, (100, 100, 200, 100))

        # Update the display
        pygame.display.update() 
        #pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

    


