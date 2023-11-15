from gamescreen import GameScreen
from constants import NewFont
from button import Button
import pygame
from animation import Sprite_Collection
from constants import WIDTH, HEIGHT

class BirdSelection(GameScreen):
    
    def __init__(self, nav) -> None:
        self.nav = nav
        self.heading = NewFont('sitkaheading', 50, 'Choose Your Player!') # TODO: Add choose your player sound file

        self.play_button = Button("Regular", WIDTH / 3 - 120, 500)
        self.ai_play_button = Button("AI Bird", WIDTH / 3 * 2 - 120, 500)
        self.type = None
        self.bird_buttons = []
        self.birds, self.types = Sprite_Collection.get_all_birds()
        for count, bird in enumerate(self.birds):
            self.bird_buttons.append(BirdButton(275 + count * 150, 200, 128, 100, bird))
        
  

    def screen_loop(self):

        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT:  
                self.running = False
                
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                if self.play_button.mouse_over():
                    if(self.type):
                        self.nav.navigate('game', self.type)

                if self.ai_play_button.mouse_over():
                    if(self.type):
                        self.nav.navigate('nn', self.type)
                        self.nav.navigate('home')
            
                for count, bird_button in enumerate(self.bird_buttons):
                    if bird_button.mouse_over():
                        self.type = self.types[count]
                        for bird in self.bird_buttons:
                            bird.active = False
                        bird_button.active = True

        
        for count, bird_button in enumerate(self.bird_buttons):
            if bird_button.mouse_over() or bird_button.active:
                self.bird_buttons[count].bg.set_alpha(255)
            else:
                self.bird_buttons[count].bg.set_alpha(0)
                    
        self.screen.fill((84,194,204))  
        
        for count, bird_button in enumerate(self.bird_buttons):
            self.screen.blit(self.bird_buttons[count].bg, self.bird_buttons[count].rect)
            self.screen.blit(self.bird_buttons[count].bird, self.bird_buttons[count].rect)
            
        self.play_button.draw(self.screen)
        self.ai_play_button.draw(self.screen)

        self.screen.blit(self.heading.render_text('Choose Your Player!'), (self.heading.horizontal_middle(), HEIGHT/7))  

class BirdButton(Button):
    def __init__(self, x, y, width, height, bird) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bird = bird
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)
        self.bg = pygame.Surface([width, height])
        self.bg.fill("red")
