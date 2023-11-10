import pygame
from navigation import Navigation
from nn_bird import NNGame


def main():
    
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load("audio/Waterflame - Glorious Morning 2.mp3")
    pygame.mixer.music.play(-1, fade_ms=3000)
    pygame.display.set_caption("Flappy Flyer")

    nav = Navigation()

    # nav.current_screen.setup
    
    while nav.current_screen.running and not isinstance(nav.current_screen, NNGame): 
        # if(isinstance(nav.current_screen, NNGame)):
        #     nav.navigate('home')
        nav.current_screen.screen_loop()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()