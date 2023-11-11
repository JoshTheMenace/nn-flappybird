import pygame
from navigation import Navigation
from constants import WIDTH, HEIGHT


def main():
    
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load("audio/Waterflame - Glorious Morning 2.mp3")
    pygame.mixer.music.play(-1, fade_ms=3000)
    pygame.display.set_caption("Flappy Flyer")

    

    nav = Navigation()
    
    while nav.current_screen.running: 
        nav.current_screen.screen_loop()
        
        pygame.display.update()
    pygame.quit()

# def sound_toggle():
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if sound_toggle.mouse_over():
#             sound_toggle.image = sound_toggle.off if sound_toggle.image == sound_toggle.on else sound_toggle.on
#             pygame.mixer.music.set_volume(0) if sound_toggle.image == sound_toggle.off else pygame.mixer.music.set_volume(1)
            
#     screen.blit(sound_toggle.image, (sound_toggle.x, sound_toggle.y)) 

if __name__ == "__main__":
    main()