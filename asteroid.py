import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self,screen):
        pygame.draw.circle(screen,WHITE,self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rangle = random.uniform(20,50)
        v1 = pygame.Vector2(self.velocity.rotate(rangle))
        v2 = pygame.Vector2(self.velocity.rotate(-rangle))
        radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x,self.position.y,radius)
        a2 = Asteroid(self.position.x,self.position.y,radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
        