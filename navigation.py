from home import Home
from game import Game
from bird_selection import BirdSelection

class Navigation:
    def __init__(self) -> None:
        self.current_screen = BirdSelection(self)

    routes = {'home': Home, 'game': Game}
    
    def navigate(self, screen, bird = None):
        if bird:
            self.current_screen = self.routes[screen](self, bird)
        else:
            self.current_screen = self.routes[screen](self)

