import pygame
from navigation import Navigation


def main():
    
    pygame.init()
    pygame.font.init()

    pygame.mixer.init()
    pygame.mixer.music.load("audio/Waterflame - Glorious Morning 2.mp3")
    pygame.mixer.music.play(-1, fade_ms=3000)

    pygame.display.set_caption("Flappy Flyer")
    icon = pygame.image.load("birds/chicken/flying/frame-2.png").convert_alpha()
    pygame.display.set_icon(icon)

    nav = Navigation()
    
    while nav.current_screen.running: 
        nav.current_screen.screen_loop()
        
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()