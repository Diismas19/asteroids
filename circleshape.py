import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen,'white',self.triangle(),2)

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self,circle_shape):
        if self.position.distance_to(circle_shape.position) <= self.radius + circle_shape.radius:
            return True
        else:
            return False