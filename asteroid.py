import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 0xFFFFFF, self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        towards = self.velocity.rotate(angle)
        away = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        first = Asteroid(self.position.x, self.position.y, radius)
        first.velocity = towards * 1.2
        second = Asteroid(self.position.x, self.position.y, radius)
        second.velocity = away * 1.2
