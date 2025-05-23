import pygame


class CircleShape(pygame.sprite.Sprite):
    """
    Base class for game objects
    """

    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # subclasses must override
        pass

    def update(self, dt):
        # subclasses must override
        pass

    def check_for_collision(self, other) -> bool:
        """
        Check if this object has collided
        with another object
        """
        return self.position.distance_to(other.position) <= self.radius + other.radius
