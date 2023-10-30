import pygame

class Bird:

    def __init__(self, screen) -> None:
        self.screen = screen

    gravity = 1
    velocity = 0
    x = 100
    y = 100
    pos = pygame.Vector2(x, y)

    r = 40

    def draw(self):
        pygame.draw.circle(self.screen, "yellow", self.pos, self.r)

    def update(self):
        self.velocity += self.gravity
        self.pos.y += self.velocity

        if(self.pos.y >= self.screen.get_height()):
            self.pos.y = self.screen.get_height()
            self.velocity = 0
        
        if(self.pos.y <= 0):
            self.pos.y = 0
            self.velocity = 0

    def jump(self):
        self.velocity = -10

        
