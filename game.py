from score import Score
import random
import pygame
from pipe import Pipe
from math import ceil
from bird import Bird
from gamescreen import GameScreen


class Game(GameScreen):

    frame_count = 0
    game_state = "play"
    pipes_sprite = pygame.sprite.Group()
    bird_sprite = pygame.sprite.GroupSingle()
    active = True
    

    def __init__(self, nav, bird_type) -> None:
        self.nav = nav
        self.score = Score()
        
        self.gamefont = pygame.font.SysFont('Comic Sans MS', 30)
        self.bg = Background(1280, 720)
        self.clock = pygame.time.Clock()
        

        self.bird = Bird(self.screen, bird_type)
        self.bird_sprite.add(self.bird)
        

    def screen_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
            if event.type == pygame.KEYDOWN and self.active == True:
                if event.key == pygame.K_SPACE:
                    self.bird.jump() if self.active == True else ""

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.active == False:
                    self.pipes_sprite.empty()
                    self.score.reset()
                    self.bird.rect.y = 50
                    self.bird.hit = False
                    self.active = True


        self.bg.update(self.screen) 
        self.bg.scroll_frame() if self.active else ""

        text_surface = self.gamefont.render(f"Score: {str(self.score.normalize())}", False, (0, 0, 0))
        

        if(self.frame_count % 120 == 0):
            if self.active == True:
                self.create_pipes()
           

        for pipe in list(self.pipes_sprite):
            if(pygame.sprite.spritecollide(self.bird, self.pipes_sprite, 0)):
                self.active = False
                self.bird.hit = True
    
            if(pipe.rect.x < 0 - Pipe.width):
                self.remove_pipe(pipe)
                self.score.increase()

        if(self.active == True):
            self.pipes_sprite.update()

        self.pipes_sprite.draw(self.screen)
        self.bird_sprite.update()
        self.bird_sprite.draw(self.screen)


                

        self.screen.blit(text_surface, (100,50))
        
        
        self.frame_count += 1
        self.clock.tick(60)


    def create_pipes(self):
        x = self.screen.get_width()
        y = self.screen.get_height()
        
        random_space_height = random.randint(150,230) # random int pixel space for bird to go through
        space_top = int(random.randint(50, y - 50 - random_space_height)) # choose a random value from y 50 to screen height - 110 
        space_bottom = space_top + random_space_height
        
        self.pipes_sprite.add(Pipe(x, 0, Pipe.width, space_top), Pipe(x, space_bottom, Pipe.width, y - space_bottom))

    def remove_pipe(self, pipe):
        self.pipes_sprite.remove(pipe)

class Background:

    def __init__(self, width, height) -> None:
        # IMAGE 
        bg = pygame.image.load("bg.png").convert() 
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
            screen.blit(self.bg, (self.bg.get_width() * i + self.scroll, 0)) 
            i += 1
       

    def scroll_frame(self):
        # FRAME FOR SCROLLING 
        self.scroll -= 2
    
        # RESET THE SCROLL FRAME 
        if abs(self.scroll) > self.bg.get_width(): 
            self.scroll = 0
