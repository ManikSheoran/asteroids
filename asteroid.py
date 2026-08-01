import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)

        ast1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        ast2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)

        ast1.velocity = self.velocity.rotate(new_angle) * 1.2
        ast2.velocity = self.velocity.rotate(-new_angle) * 1.2
