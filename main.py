import pygame
from bird import Bird
from bad_pipes import Pipes
from game import Game


def main():
    
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    game = Game(screen)
    clock = pygame.time.Clock()
    running = True
    dt = 0
    bird = Bird(screen)
    pipes = Pipes(game)
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN and game.active == True:
                if event.key == pygame.K_SPACE:
                    bird.jump()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     game.active = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("aqua")

        if(game.frame_count % 120 == 0):
            pipes.create_pipe() if game.active == True else ""

        if(game.active == True):
            bird.update()
        bird.draw()

        for pipe in pipes.pipes:
            if(pipe.check_collision(bird)):
                game.active = False
            
            pipe.update() if game.active == True else ""
            pipe.draw(screen, "green")
            if(pipe.x < 0):
                pipes.remove_pipe(pipe)
                

                
        
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        game.frame_count += 1
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()