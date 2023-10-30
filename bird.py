import pygame

class Bird:

    def __init__(self, screen) -> None:
        self.screen = screen

    gravity = 0.8
    velocity = 0
    jump_val = -12

    pos = pygame.Vector2(100, 100)

    r = 20

    def draw(self):
        pygame.draw.circle(self.screen, "yellow", self.pos, self.r)

    def update(self):
        self.velocity += self.gravity
        # self.velocity *= 0.9
        self.pos.y += self.velocity

        if(self.pos.y >= self.screen.get_height()): # restrict y bottom
            self.pos.y = self.screen.get_height()
            self.velocity = 0
        
        if(self.pos.y <= 0): # restrict y top
            self.pos.y = 0
            self.velocity = 0

    def jump(self):
        if (self.velocity > -5): # if the last jump was 7 frames or more ago
            self.velocity = self.jump_val
            

        
