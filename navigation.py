from home import Home
from game import Game

class Navigation:
    def __init__(self) -> None:
        self.current_screen = Home(self)

    routes = {'home': Home, 'game': Game}
    
    def navigate(self, screen):
        self.current_screen = self.routes[screen](self)

