import pygame  
from main import main
from constants import Constants, NewFont, HEIGHT, WIDTH
from button import Button
  


# initializing the constructor  
pygame.init()  
  

heading = NewFont('sitkaheading', 60, 'Flapping Birds')


# opens up a window  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  

button = Button("Play", 100, 500)
  


  
while True: 
      
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
        if ev.type == pygame.MOUSEBUTTONDOWN:  
            
            if button.mouse_over():
                main()
 

                  
    screen.fill((84,194,204))  
      

    button.draw(screen)

      
      
    screen.blit(heading.render_text('Flappy Birds'), (heading.horizontal_middle(), HEIGHT/6))  
      
    # updates the frames of the game  
    pygame.display.update()  