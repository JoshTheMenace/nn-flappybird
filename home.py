import pygame  
from constants import NewFont, HEIGHT, WIDTH, CYAN
from button import Button
from gamescreen import GameScreen


class Home(GameScreen):
    
    def __init__(self, nav) -> None:
        self.nav = nav
        self.heading = NewFont('sitkaheading', 60, 'Flappy Flyer')
        self.sub_title = NewFont('trebuchet', 35, 'By: Josh Gimenes')

        self.select_button = Button("Select Bird", WIDTH / 2 - 120, 500)


    def screen_loop(self):
        for ev in pygame.event.get():  
          
            if ev.type == pygame.QUIT:  
                self.running = False
                
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                
                if self.select_button.mouse_over():
                    self.nav.navigate('selection')
                    
        self.screen.fill(CYAN)  
        self.select_button.draw(self.screen)

        self.screen.blit(self.heading.render_text('Flappy Flyer'), (self.heading.horizontal_middle(), HEIGHT/6))  
        self.screen.blit(self.sub_title.render_text('By: Josh Gimenes'), (self.sub_title.horizontal_middle(), HEIGHT/3))  
  