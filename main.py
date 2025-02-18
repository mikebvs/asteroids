import pygame # https://www.pygame.org/docs/ref/pygame.html
from constants import *

def main():
    print(f"Starting asteroids! Running resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting asteroids!")
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()