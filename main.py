import pygame # https://www.pygame.org/docs/ref/pygame.html
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting asteroids! Running resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    # Init Pygame
    pygame.init()

    # Pygame Clock
    clock = pygame.time.Clock()
    dt = 0

    # Pygame Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add Pygame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Update Player containers
    Player.Containers = updatable, drawable
    # Instantiate Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Update AsteroidField containers
    AsteroidField.containers = updatable
    # Instantiate AsteroidField
    asteroidfield = AsteroidField()

    # Update Asteroid containers
    Asteroid.containers = updatable, drawable, asteroids
    
    # Update Shot containers
    Shot.containers = updatable, drawable, shots

    # Add objects to Pygame Groups
    # Add to Updatable Group
    updatable.add(player)
    updatable.add(asteroidfield)
    updatable.add(asteroids)
    # Add to Drawable Group
    drawable.add(player)
    drawable.add(asteroids)

    # Game running loop
    while True:
        # Game exit check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting asteroids!")
                return

        # Update clock timing and convert to seconds 
        dt = clock.tick(60)/1000
        
        # Black Background Screen
        screen.fill((0, 0, 0))

        # Update game objects - Player
        updatable.update(dt)
        shots.update(dt)

        # Draw game objects - Player
        for drawings in drawable:
            drawings.draw(screen)
        
        # Render new frame
        pygame.display.flip()

        # Check for collisions
        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                print("Game over!")
                return

if __name__ == "__main__":
    main()