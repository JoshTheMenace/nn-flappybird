import random
import pygame

class Pipe:
    width = 50
    speed = 4

    def __init__(self, x, height, space_top, space_bottom) -> None:
        self.x = x
        self.space_top = space_top
        self.space_bottom = space_bottom
        self.height = height

    def update(self):
        self.x -= self.speed

    def draw(self, screen, color):
        top = pygame.Rect(self.x, 0, Pipe.width, self.space_top)
        bottom = pygame.Rect(self.x, self.space_bottom, Pipe.width, self.height - self.space_bottom)
        pygame.draw.rect(screen, color, top, self.width)
        pygame.draw.rect(screen, color, bottom, self.width)

    def check_collision(self, bird):
        top = pygame.Rect(self.x, 0, Pipe.width, self.space_top)
        bottom = pygame.Rect(self.x, self.space_bottom, Pipe.width, self.height - self.space_bottom)
        return top.collidepoint(bird.pos.x, bird.pos.y) or bottom.collidepoint(bird.pos.x, bird.pos.y)



class Pipes:
    pipes = []

    def __init__(self, game) -> None:
        self.game = game
        self.width = self.game.screen.get_width()
        self.height = self.game.screen.get_height()
       
    
    def create_pipe(self):
        
        space_top = int(random.randint(50, self.height - 110)) # choose a random value from y 50 to screen height - 110 
        space_bottom = space_top + 100 # 100 pixel space for bird to go through
        
        self.pipes.append(Pipe(self.width, self.height, space_top, space_bottom))
    
    def remove_pipe(self, pipe):
        self.pipes.remove(pipe)
    
            
