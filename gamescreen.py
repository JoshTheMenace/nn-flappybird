from abc import ABC, abstractmethod
from pygame import display

class GameScreen(ABC):
    running = True
    screen = display.set_mode((1280, 720))

    @abstractmethod
    def screen_loop():
        pass
