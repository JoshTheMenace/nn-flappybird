import pygame


class Pipe(pygame.sprite.Sprite):
    width = 70
    speed = 4

    def __init__(self, x, top, width, height) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([Pipe.width, height])
        self.image.fill("green")

        self.rect = pygame.Rect(x, top, width, height)

    def update(self):
        self.rect.x -= self.speed

    def draw(self):
        pass


