import pygame  
# from main import main
from constants import NewFont, HEIGHT, WIDTH, CYAN
from button import Button
from gamescreen import GameScreen



class Home(GameScreen):
    
    def __init__(self, nav) -> None:
        self.nav = nav
        self.heading = NewFont('sitkaheading', 60, 'Flappy Flyer')

        self.button = Button("Play", 100, 500)
        self.button2 = Button("NN", 600, 500)

  

    def screen_loop(self):
        for ev in pygame.event.get():  
          
            if ev.type == pygame.QUIT:  
                self.running = False
                
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                
                if self.button.mouse_over():
                    self.nav.navigate('selection')
                if self.button2.mouse_over():
                    self.nav.navigate('nn')
    

                    
        self.screen.fill(CYAN)  
        

        self.button.draw(self.screen)
        self.button2.draw(self.screen)

        self.screen.blit(self.heading.render_text('Flappy Flyer'), (self.heading.horizontal_middle(), HEIGHT/6))  
  
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