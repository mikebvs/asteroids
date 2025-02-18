import pygame # https://www.pygame.org/docs/ref/pygame.html
from constants import *
from player import Player

def main():
    print(f"Starting asteroids! Running resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting asteroids!")
                return
            
        dt = clock.tick(60)/1000
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()