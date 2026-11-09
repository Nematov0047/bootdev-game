from circleshape import CircleShape
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, PLAYER_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, PLAYER_RADIUS, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        randomAngle = random.uniform(20, 50)
        newVector = self.velocity.rotate(randomAngle)
        secondNewVector = self.velocity.rotate(-randomAngle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS
        firstNewAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
        secondNewAsteroid = Asteroid(self.position.x, self.position.y, newRadius)

        firstNewAsteroid.velocity = newVector * 1.2
        secondNewAsteroid.velocity = secondNewVector * 1.2

