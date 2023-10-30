import random
import pygame

class Pipe:

    width = 50
    speed = 4

    def __init__(self, screen) -> None:
        self.screen = screen
        rand_h_pos = int(random.randint(50, self.screen.get_height() - 110))
        self.space_top = rand_h_pos
        # self.space_top = self.screen.get_height() - 100
        self.space_bottom = self.space_top + 100
        self.x = self.screen.get_width()

        # self.top = pygame.Rect(self.x, 0, self.width, self.space_top)
        # self.bottom = pygame.Rect(self.x, self.space_bottom, self.width, self.screen.get_height() - self.space_bottom)
    
    # rand_h_pos = random.randint(0, self.screen)
    
    

    
    def draw(self):
        self.top = pygame.Rect(self.x, 0, self.width, self.space_top)
        pygame.draw.rect(self.screen, "green", self.top, self.width)
        self.bottom = pygame.Rect(self.x, self.space_bottom, self.width, self.screen.get_height() - self.space_bottom)
        pygame.draw.rect(self.screen, "green", self.bottom, self.width)

    def update(self):
        self.x -= self.speed

    def check_collision(self, bird):
        top = pygame.Rect(self.x, 0, self.width, self.space_top)
        bottom = pygame.Rect(self.x, self.space_bottom, self.width, self.screen.get_height() - self.space_bottom)
        return top.collidepoint(bird.pos.x, bird.pos.y) or bottom.collidepoint(bird.pos.x, bird.pos.y)
            
