from score import Score
import random
import pygame
from pipe import Pipe, BluePipe
from math import ceil
from bird import Bird
from gamescreen import GameScreen
from button import Button
from overlay import Overlay
from constants import WIDTH, HEIGHT, CYAN, NewFont
import neat


class NNGame(GameScreen):

    frame_count = 0
    game_state = "play"
    pipes_sprite = pygame.sprite.Group()
    bird_sprite = pygame.sprite.Group()
    
    active = True
    pause_overlay = Overlay()
    

    def __init__(self, nav, bird_type) -> None:
        self.nav = nav
        self.score = Score()
        
        self.gamefont = pygame.font.SysFont('sitkabanner', 25)
        self.bg = Background(WIDTH, HEIGHT)
        self.clock = pygame.time.Clock()
        
        self.bird_type = bird_type
        self.gamespeed = 60

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.crash_sound = pygame.mixer.Sound('audio/crash.mp3')
        self.jump_sound.set_volume(0.5)
        self.crash_sound.set_volume(0.5)

        self.death_screen = pygame.Surface((WIDTH / 3 * 2, HEIGHT / 3 * 2))
        self.death_screen_rect = pygame.Rect(WIDTH / 6, HEIGHT / 6, WIDTH / 3 * 2, HEIGHT / 3 * 2)
        self.death_screen.fill(CYAN)

        self.gameover = NewFont('sitkaheading', 60, 'Game Over')
        self.play_button = Button("Play Again", WIDTH/2 + Button.width / 6, HEIGHT/3*2)
        self.home_button = Button("Home", WIDTH/2 - Button.width - Button.width / 6, HEIGHT/3*2)

        self.ff_toggle = ToggleButton(WIDTH-150, 25, 50, 50, ["images/ff_on.png","images/ff_off.png"])
        self.sound_toggle = ToggleButton(WIDTH-75, 25, 50, 50, ["images/sound_on.png","images/sound_off.png"])

        self.config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         "nn_config.txt")
        p = neat.Population(self.config)
         # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        self.gen = 0
        self.run = True
        # Run for up to 50 generations.
        try:
            p.run(self.screen_loop, 50)
        except TypeError: # catch error to break out of training loop
            pass


        
    def reset_game(self):
        self.pipes_sprite.empty()
        self.bird_sprite.empty()
        self.score.reset()
        for bird in self.birds:
            bird.rect.y = 50
            bird.hit = False
        self.active = True

    def screen_loop(self, genomes, config):
        self.gen += 1
        nets = []
        self.birds = []
        ge = []
        for genome_id, genome in genomes:
            if not self.run: 
                break
            genome.fitness = 0  # start with fitness level of 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            bird = Bird(self.screen, self.bird_type)
            self.birds.append(bird)
            self.bird_sprite.add(bird)
            ge.append(genome)
        
        while self.run and len(self.birds) > 0:
            pipes = list(self.pipes_sprite)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.active == True:
                        if self.active:
                            self.jump_sound.play()
                            for bird in self.birds:
                                bird.jump()
                    if event.key == pygame.K_ESCAPE:
                        self.active = False if self.active else True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.mouse_over():
                        if self.active == False:
                            self.reset_game()
                    if self.home_button.mouse_over():
                        self.reset_game()
                        self.nav.navigate('home')
                        self.run = False
                        raise TypeError("Break out")
                    if self.ff_toggle.mouse_over() and self.active:
                        self.ff_toggle.image = self.ff_toggle.on if self.ff_toggle.image == self.ff_toggle.off else self.ff_toggle.off
                        self.gamespeed = 120 if self.ff_toggle.image == self.ff_toggle.on else 60
                    if self.sound_toggle.mouse_over():
                        self.sound_toggle.image = self.sound_toggle.on if self.sound_toggle.image == self.sound_toggle.off else self.sound_toggle.off
                        pygame.mixer.music.set_volume(0) if self.sound_toggle.image == self.sound_toggle.on else pygame.mixer.music.set_volume(1)

            pipe_ind = 0
            
            if len(pipes) > 0:
                for x, bird in enumerate(self.birds):  # give each bird a fitness of 0.1 for each frame it stays alive
                    ge[x].fitness += 0.1

                    # send bird location, top pipe location and bottom pipe location and determine from network whether to jump or not
                    output = nets[self.birds.index(bird)].activate((bird.rect.y, abs(bird.rect.y - pipes[pipe_ind].rect.height), abs(bird.rect.y - pipes[pipe_ind + 1].rect.top)))

                    if output[0] > 0.5:  # we use a tanh activation function so result will be between -1 and 1. if over 0.5, jump
                        bird.jump()

            self.bg.update(self.screen) 
            self.bg.scroll_frame() if self.active else ""

            score_surface = self.gamefont.render(f"Score: {str(self.score.normalize())}", False, (0, 0, 0))
            bird_count_surface = self.gamefont.render(f"Bird Count: {str(len(self.birds))}", False, (0, 0, 0))
            gen_surface = self.gamefont.render(f"Generation: {str(self.gen)}", False, (0, 0, 0))
            

            if(self.frame_count % 120 == 0):
                if self.active == True:
                    self.create_pipes()
            
            for bird in self.birds:
                if(bird.rect.bottom >= self.screen.get_height()): # restrict y bottom
                    ge[self.birds.index(bird)].fitness -= 0.1
                if(bird.rect.y <= 0): # restrict y top
                    ge[self.birds.index(bird)].fitness -= 0.1

                if(pygame.sprite.spritecollide(bird, list(self.pipes_sprite), 0)):
                    self.crash_sound.play() if self.active else ""
                    ge[self.birds.index(bird)].fitness -= 1
                    nets.pop(self.birds.index(bird))
                    ge.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))
                    self.bird_sprite.remove(bird)
                    
           
            if len(self.birds) == 0:
                self.reset_game()
                    
            for pipe in list(self.pipes_sprite):
                if(pipe.rect.x < 0 - Pipe.width):
                    self.remove_pipe(pipe)
                    self.score.increase()
                    for genome in ge:
                        genome.fitness += 5

            if(self.active == True):
                self.pipes_sprite.update()

            self.pipes_sprite.draw(self.screen)
            
            self.bird_sprite.update()
            self.bird_sprite.draw(self.screen)


            self.screen.blit(score_surface, (100,25))
            self.screen.blit(bird_count_surface, (100,75))
            self.screen.blit(gen_surface, (100,125))

            self.screen.blit(self.ff_toggle.image, (self.ff_toggle.x, self.ff_toggle.y)) 
            
            if not self.active:
                self.screen.blit(self.pause_overlay.bg, self.pause_overlay.rect)
                self.screen.blit(self.death_screen, self.death_screen_rect)
                self.screen.blit(self.gameover.render_text('Game Paused'), (self.gameover.horizontal_middle(), HEIGHT/3))  
                self.home_button.draw(self.screen)
                self.play_button.draw(self.screen)

            self.screen.blit(self.sound_toggle.image, (self.sound_toggle.x, self.sound_toggle.y)) 

            self.frame_count += 1
            self.clock.tick(self.gamespeed)

            pygame.display.update()

    def create_pipes(self):
        blue_chance = random.randint(0,3)
        x = self.screen.get_width()
        y = self.screen.get_height()
        if blue_chance == 0:
            random_space_height = random.randint(175,240) # Extra space for blue moving pipes
        else:
            random_space_height = random.randint(150,230) # random int pixel space for bird to go through
        space_top = int(random.randint(50, y - 50 - random_space_height)) # choose a random value from y 50 to screen height - 110 
        space_bottom = space_top + random_space_height
        direction = random.choice([1,-1])
        if blue_chance == 0:
            self.pipes_sprite.add(BluePipe(x, 0, Pipe.width, space_top, random_space_height, direction), BluePipe(x, space_bottom, Pipe.width, y - space_bottom, random_space_height, direction))
        else:
            self.pipes_sprite.add(Pipe(x, 0, Pipe.width, space_top), Pipe(x, space_bottom, Pipe.width, y - space_bottom))
        

    def remove_pipe(self, pipe):
        self.pipes_sprite.remove(pipe)

class Background:

    def __init__(self, width, height) -> None:
        bg = pygame.image.load("images/bg.png").convert() 
        self.bg = pygame.transform.scale(bg, (width, height))
        
        self.scroll = 0
        self.tiles = ceil(width / bg.get_width()) + 1

    def update(self, screen):
        i = 0
        while(i < self.tiles): 
            screen.blit(self.bg, (self.bg.get_width() * i + self.scroll, 0)) 
            i += 1
       

    def scroll_frame(self):
        self.scroll -= 2
    
        if abs(self.scroll) > self.bg.get_width(): 
            self.scroll = 0


class ToggleButton(Button):
    def __init__(self, x, y, width, height, images: []) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        off = pygame.image.load(images[0]).convert_alpha()
        self.off = pygame.transform.scale(off, (width, height))
        on = pygame.image.load(images[1]).convert_alpha()
        self.on = pygame.transform.scale(on, (width, height))
        self.image = self.off
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)
        self.bg = pygame.Surface([width, height])