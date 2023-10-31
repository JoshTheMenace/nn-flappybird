import pygame
# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 254) 
BLUE     = (   0,   0, 255)

class Bird(pygame.sprite.Sprite):

    def __init__(self, screen) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("bird.png").convert_alpha()
        # self.image = pygame.Surface([10,10])
 
        # Set our transparent color
        # self.image.set_colorkey(WHITE)
        # self.image.fill("red")

        self.rect = self.image.get_rect()
        # self.rect.height = 100
        # self.rect.width = 100
    gravity = 0.8
    velocity = 0
    jump_val = -12

    # pos = pygame.Vector2(100, 100)

    r = 20

    def draw(self):
        pass
        # pygame.draw.circle(self.screen, "yellow", self.pos, self.r)

    def update(self):
        self.velocity += self.gravity
        # self.velocity *= 0.9
        self.rect.y += self.velocity

        if(self.rect.bottom >= self.screen.get_height()): # restrict y bottom
            self.rect.bottom = self.screen.get_height()
            self.velocity = 0
        
        if(self.rect.y <= 0): # restrict y top
            self.rect.y = 0
            self.velocity = 0

    def jump(self):
        if (self.velocity > -5): # if the last jump was 7 frames or more ago
            self.velocity = self.jump_val
            

        
