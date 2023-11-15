import pygame
from animation import Sprite_Collection
import math


class Bird(pygame.sprite.Sprite):

    def __init__(self, screen, type) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.sprites = Sprite_Collection(type)

        self.images = self.sprites.alive_images
        self.index = 0
        self.screen = screen
        self.hit = False
        self.image = self.images[math.ceil(self.index)]

        self.rect = self.image.get_rect()
        self.rect.y = 200

    gravity = 0.8
    velocity = 0
    jump_val = -11


    def update(self):
        
        self.images = self.sprites.alive_images if self.hit == False else self.sprites.dead_images
        self.index += (0.1 * self.sprites.factor) if self.hit else 0.1

        if math.ceil(self.index) > len(self.images) -1:
            self.index = 0

        self.image = self.images[math.ceil(self.index)]

        self.velocity += self.gravity
        self.rect.y += self.velocity

        if(self.rect.bottom >= self.screen.get_height()): # restrict y bottom
            self.rect.bottom = self.screen.get_height()
            self.velocity = 0
        
        if(self.rect.y <= 0): # restrict y top
            self.rect.y = 0
            self.velocity = 0

    def jump(self):
        if (self.velocity > -5): # if the last jump was 6 frames or more ago
            self.velocity = self.jump_val
