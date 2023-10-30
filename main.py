import pygame
from bird import Bird
from pipe import Pipe
from game import Game


def main():
    game = Game()
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    bird = Bird(screen)
    pipes = []
    # pipe = Pipe(screen)
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN and game.active == True:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("aqua")

        # print(pipes)
        if(game.frame_count % 120 == 0):
            pipes.append(Pipe(screen))

        if(game.active == True):
            bird.update()
        bird.draw()

        for pipe in pipes:
            if(pipe.check_collision(bird)):
                game.active = False
                for p in pipes:
                    p.speed = 0
            pipe.update()
            pipe.draw()
            if(pipe.x < 0):
                pipes.remove(pipe)

                
        
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        game.frame_count += 1
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()