import pygame


class Bird(pygame.sprite.Sprite):

    def __init__(self, screen) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("bird.png").convert_alpha()

        self.rect = self.image.get_rect()

    gravity = 0.8
    velocity = 0
    jump_val = -12


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
            

        
