import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    """
    Class to represent an asteroid
    inherits from `CircleShape`
    """

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        """
        Draws an asteroid on the screen
        """
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        """
        Override the `update` method from `CircleShape`
        """
        self.position += self.velocity * dt

    def split(self):
        """
        Split the asteroid into smaller asteroids
        IF the asteroid is larger than the minimum size
        """
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)

            velocity1 = self.velocity.rotate(split_angle)
            velocity2 = self.velocity.rotate(-split_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2
