import pygame
from navigation import Navigation


def main():
    
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Flapping Birds")

    nav = Navigation()


    while nav.current_screen.running:

        nav.current_screen.screen_loop()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()