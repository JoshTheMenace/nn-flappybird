import pygame
from constants import HEIGHT


class Pipe(pygame.sprite.Sprite):
    width = 70
    speed = 4

    def __init__(self, x, top, width, height) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([Pipe.width, height])
        self.image.fill('green')
        self.rect = pygame.Rect(x, top, width, height)

    def update(self):
        self.rect.x -= self.speed


class BluePipe(Pipe, pygame.sprite.Sprite):
    width = 70
    speed = 4
    yspeed = 2

    def __init__(self, x, top, width, height, gap_distance, direction) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.type = "top" if top == 0 else "bottom"
        self.gap_distance = gap_distance
            
        self.image = pygame.Surface([Pipe.width, height])
        self.image.fill('blue')
        self.rect = pygame.Rect(x, top, width, height)

        self.direction = direction

    def update(self):
        self.rect.x -= self.speed
        if self.direction == 1:
            if self.rect.top == 0:
                if self.rect.height <= self.yspeed * 3:
                    self.direction = -1
                self.rect = pygame.Rect(self.rect.x, self.rect.top, self.rect.width, self.rect.height - self.yspeed)
                self.image = pygame.Surface([Pipe.width, self.rect.height - self.yspeed])
                self.image.fill('blue')
            else:
                if self.rect.top < self.gap_distance + self.yspeed * 3:
                    self.direction = -1
                self.rect = pygame.Rect(self.rect.x, self.rect.top - self.yspeed, self.rect.width, self.rect.height + self.yspeed)
                self.image = pygame.Surface([Pipe.width, self.rect.height + self.yspeed])
                self.image.fill('blue')
                
        else:
            if self.rect.top == 0:
                if HEIGHT - self.rect.bottom < self.gap_distance + self.yspeed * 3:
                    self.direction = 1
                self.rect = pygame.Rect(self.rect.x, self.rect.top, self.rect.width, self.rect.height + self.yspeed)
                self.image = pygame.Surface([Pipe.width, self.rect.height + self.yspeed])
                self.image.fill('blue')
            else:
                if self.rect.height <= self.yspeed * 3:
                    self.direction = 1
                self.rect = pygame.Rect(self.rect.x, self.rect.top + self.yspeed, self.rect.width, self.rect.height - self.yspeed)
                self.image = pygame.Surface([Pipe.width, self.rect.height - self.yspeed])
                self.image.fill('blue')

