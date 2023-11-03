import pygame  
# from main import main
from constants import NewFont, HEIGHT, WIDTH
from button import Button
from gamescreen import GameScreen



class Home(GameScreen):
    
    def __init__(self, nav) -> None:
        self.nav = nav
        self.heading = NewFont('sitkaheading', 60, 'Flapping Birds')

        self.button = Button("Play", 100, 500)

  

    def screen_loop(self):
        for ev in pygame.event.get():  
          
            if ev.type == pygame.QUIT:  
                self.running = False
                
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                
                if self.button.mouse_over():
                    self.nav.navigate('selection')
    

                    
        self.screen.fill((84,194,204))  
        

        self.button.draw(self.screen)

        self.screen.blit(self.heading.render_text('Flappy Birds'), (self.heading.horizontal_middle(), HEIGHT/6))  
  
# while True: 
      
#     for ev in pygame.event.get():  
          
#         if ev.type == pygame.QUIT:  
#             pygame.quit()  
              
#         if ev.type == pygame.MOUSEBUTTONDOWN:  
            
#             if button.mouse_over():
#                 main()
    

                  
#     screen.fill((84,194,204))  
      

#     button.draw(screen)

      
      
#     screen.blit(heading.render_text('Flappy Birds'), (heading.horizontal_middle(), HEIGHT/6))  
      
#     # updates the frames of the game  
#     pygame.display.update()  