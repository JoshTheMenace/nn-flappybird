from score import Score
import random
import pygame
from pipe import Pipe
from math import ceil

class Game:
    
    frame_count = 0
    game_state = "play"
    pipes_sprite = pygame.sprite.Group()
    bird_sprite = pygame.sprite.GroupSingle()
    active = True

    def __init__(self, screen) -> None:
        self.screen = screen
        self.score = Score()


    def create_pipes(self):
        x = self.screen.get_width()
        y = self.screen.get_height()
        
        random_space_height = random.randint(115,230) # random int pixel space for bird to go through
        space_top = int(random.randint(50, y - 50 - random_space_height)) # choose a random value from y 50 to screen height - 110 
        space_bottom = space_top + random_space_height
        
        self.pipes_sprite.add(Pipe(x, 0, Pipe.width, space_top), Pipe(x, space_bottom, Pipe.width, y - space_bottom))

    def remove_pipe(self, pipe):
        self.pipes_sprite.remove(pipe)

class Background:

    def __init__(self, width, height) -> None:
        # IMAGE 
        bg = pygame.image.load("tree.png").convert() 
        self.bg = pygame.transform.scale(bg, (width, height))
        
        # DEFINING MAIN VARIABLES IN SCROLLING 
        self.scroll = 0
        
        # CHANGE THE BELOW 1 TO UPPER NUMBER IF 
        # YOU GET BUFFERING OF THE IMAGE 
        # HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING 
        self.tiles = ceil(width / bg.get_width()) + 1

    def update(self, screen):
        i = 0
        while(i < self.tiles): 
            screen.blit(self.bg, (self.bg.get_width()*i 
                            + self.scroll, 0)) 
            i += 1
       

    def scroll_frame(self):
        # FRAME FOR SCROLLING 
        self.scroll -= 2
    
        # RESET THE SCROLL FRAME 
        if abs(self.scroll) > self.bg.get_width(): 
            self.scroll = 0
