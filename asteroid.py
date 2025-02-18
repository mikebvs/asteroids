from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.field = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            angle = random.randint(20, 50)
            negative_angle = -angle
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(negative_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius).velocity = velocity1 * 1.2
            Asteroid(self.position.x, self.position.y, new_asteroid_radius).velocity = velocity2