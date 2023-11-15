from pygame import Surface
from constants import WIDTH, HEIGHT

class Overlay():
    def __init__(self) -> None:
        self.bg = Surface([WIDTH, HEIGHT])
        self.bg.fill("black")
        self.bg.set_alpha(100)
        self.rect = self.bg.get_rect()
