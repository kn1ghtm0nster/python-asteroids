import pygame

from circleshape import CircleShape


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
