import pygame
from bird import Bird
from pipe import Pipe
from game import Game


def main():
    
    # pygame setup
    pygame.init()
    pygame.font.init()
    gamefont = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((1280, 720))
    game = Game(screen)
    clock = pygame.time.Clock()
    running = True

    bird = Bird(screen)
    game.bird_sprite.add(bird)
    dt = 0
    

    # pipes = Pipes(game)

    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN and game.active == True:
                if event.key == pygame.K_SPACE:
                    bird.jump() if game.active == True else ""

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.active == False:
                    game.pipes_sprite.empty()
                    game.score.reset()
                    bird.rect.y = 50
                    game.active = True

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("aqua")

        text_surface = gamefont.render(f"Score: {str(game.score.normalize())}", False, (0, 0, 0))
        # This creates a new surface with text already drawn onto it. At the end you can just blit the text surface onto your main screen.

        

        if(game.frame_count % 120 == 0):
            if game.active == True:
                game.create_pipes()
           

        for pipe in list(game.pipes_sprite):
            if(pygame.sprite.spritecollide(bird, game.pipes_sprite, 0)):
                game.active = False
            # if(pipe.check_collision(bird)):
            # if(pygame.sprite.collide_rect(pipe, bird)):
                # game.active = False
            
            # pipe.update() if game.active == True else ""
            # pipe.draw(screen, "green")
            if(pipe.rect.x < 0 - Pipe.width):
                game.remove_pipe(pipe)
                game.score.increase()

        if(game.active == True):
            game.pipes_sprite.update()
            # game.bird_sprite.update()

        game.pipes_sprite.draw(screen)
        game.bird_sprite.update()
        game.bird_sprite.draw(screen)


                

        screen.blit(text_surface, (100,50))
        
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        game.frame_count += 1
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()