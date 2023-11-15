
from pygame import font

WIDTH = 1280
HEIGHT = 720
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 254) 
BLUE     = (   0,   0, 255)
CYAN = (84,194,204)
ORANGE = (229, 95, 0)
GREEN = (175, 226, 86)

class NewFont():
    button_font = 'trebuchetms'
    button_size = 32

    def __init__(self, name: str, size: int, text) -> None:
        
        self.f = font.SysFont(name, size)
        self.text = text
        
    @property
    def width(self):
        return self.f.size(self.text)[0]
    
    @property
    def height(self):
        return self.f.size(self.text)[1]
    
    def render_text(self, text, color = "white"):
        return self.f.render(text , True , color)
    
    def horizontal_middle(self):
        return (WIDTH / 2) - (self.width / 2)
    
    def button_middle(self, button):
        middle_x = button.x + (button.width / 2) - (self.width / 2)
        middle_y = button.y + (button.height / 2) - (self.height / 2)

        return (middle_x, middle_y)
