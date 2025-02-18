from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_SPIRAL_SHOT_MODIFIER, PLAYER_COLLISION_COOLDOWN, PLAYER_RADIAL_SHOT_COOLDOWN, PLAYER_SPIRAL_SHOT_DURATION, PLAYER_SPIRAL_SHOT_COOLDOWN, PLAYER_LIVES
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.field = 0 
        self.rotation = 0
        self.fire_rate_cooldown = 0
        self.radial_shot_cooldown = 0
        self.__radial_shot_modifier = 30
        self.collision_cooldown = 0
        self.lives = PLAYER_LIVES
        self.spiral_shot_cooldown = 0
        self.__spiral_shot_duration = 0
        self.__spiral_shot_value = 0
        self.__spiral_shot_modifier = PLAYER_SPIRAL_SHOT_MODIFIER

    def draw(self, screen):
        rate = 8
        if self.collision_cooldown == 0:
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
        elif (self.collision_cooldown * rate).__floor__() % 2 == 0:
            pygame.draw.polygon(screen, (255, 0, 0), self.triangle())
        elif (self.collision_cooldown * rate).__floor__() % 2 == 1:
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
        else:
            pygame.draw.polygon(screen, (255, 0, 0), self.triangle())

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.fire_rate_cooldown == 0:
            self.shoot()
        if keys[pygame.K_q] and self.radial_shot_cooldown == 0:
            self.radial_shot()
        if keys[pygame.K_e] and self.spiral_shot_cooldown == 0:
            self.spiral_shot_activate()
        
        # Update Cooldowns
        # Fire Rate
        if self.fire_rate_cooldown > 0:
            self.fire_rate_cooldown -= dt
            if self.fire_rate_cooldown < 0:
                self.fire_rate_cooldown = 0
        # Radial Shot
        if self.radial_shot_cooldown > 0:
            self.radial_shot_cooldown -= dt
            if self.radial_shot_cooldown < 0:
                self.radial_shot_cooldown = 0
        # Spiral Shot
        if self.spiral_shot_cooldown > 0:
            self.spiral_shot_cooldown -= dt
            if self.spiral_shot_cooldown < 0:
                self.spiral_shot_cooldown = 0
        # Collision Cooldown
        if self.collision_cooldown > 0:
            self.collision_cooldown -= dt
            if self.collision_cooldown < 0:
                self.collision_cooldown = 0
        
        # Duration Based Effects
        if self.__spiral_shot_duration > 0:
            self.__spiral_shot_duration -= dt
            # If the duration is a NEW whole number, then shoot using using the new rotation
            if (self.__spiral_shot_duration * self.__spiral_shot_modifier).__floor__() != self.__spiral_shot_value:
                self.__spiral_shot_value = (self.__spiral_shot_duration * self.__spiral_shot_modifier).__floor__()
                rotation = ((self.__spiral_shot_duration * self.__spiral_shot_modifier).__floor__() * 30)
                self.spiral_shot(rotation)
            if self.__spiral_shot_duration < 0:
                self.__spiral_shot_duration = 0

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, 2)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.fire_rate_cooldown = PLAYER_SHOOT_COOLDOWN
        
    def radial_shot(self):
        rotation = 360 / self.__radial_shot_modifier
        for i in range(0, self.__radial_shot_modifier):
            shot = Shot(self.position.x, self.position.y, 2)
            shot.velocity = pygame.Vector2(0, 1).rotate(i * rotation) * PLAYER_SHOOT_SPEED
            self.radial_shot_cooldown = PLAYER_RADIAL_SHOT_COOLDOWN

    def spiral_shot_activate(self):
        self.spiral_shot_cooldown = PLAYER_SPIRAL_SHOT_COOLDOWN
        self.__spiral_shot_duration = PLAYER_SPIRAL_SHOT_DURATION
        self.__spiral_shot_value = PLAYER_SPIRAL_SHOT_DURATION * self.__spiral_shot_modifier
    
    def spiral_shot(self, rotation):
        shot = Shot(self.position.x, self.position.y, 2)
        shot.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def collided(self):
        self.collision_cooldown = PLAYER_COLLISION_COOLDOWN