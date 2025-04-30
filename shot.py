import pygame


from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """
    Class to represent a single shot
    inherits from `CircleShape`
    """

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen) -> None:
        """
        Draws a shot on the screen
        """
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt) -> None:
        """
        Override the `update` method from `CircleShape`
        """
        self.position += self.velocity * dt
