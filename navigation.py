from home import Home
from game import Game
from bird_selection import BirdSelection
import nn_bird

class Navigation:
    def __init__(self) -> None:
        self.current_screen = Home(self)

    routes = {'home': Home, 'game': Game, 'selection': BirdSelection, 'nn': nn_bird.NNGame}
    
    def navigate(self, screen, bird = 'chicken'):
        if screen == 'nn' or screen == 'game':
            self.current_screen = self.routes[screen](self, bird)
        else:
            self.current_screen = self.routes[screen](self)

