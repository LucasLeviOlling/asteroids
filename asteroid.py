import pygame
import circleshape
import constants
import random
from logger import log_state, log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            r1 = self.velocity.rotate(angle)
            r2 = self.velocity.rotate(angle * -1)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            baby1 = Asteroid(self.position[0], self.position[1], new_radius)
            baby2 = Asteroid(self.position[0], self.position[1], new_radius)
            baby1.velocity = r1 * 1.2
            baby2.velocity = r2 * 1.2
