from pygame import mouse, Rect, draw
from constants import NewFont

class Button():
    width = 240
    height = 100
    color = 'orange'
    hover_color = 'yellow'
    text_color = 'white'
    text_hover_color = 'black'

    def __init__(self, text, x, y) -> None:
        self.text = text
        self.x = x
        self.y = y
        self.font = NewFont(NewFont.button_font, NewFont.button_size, text)


    def draw(self, screen):
        hovering = self.mouse_over()

        color = self.hover_color if hovering else self.color
        draw.rect(screen, color, Rect(self.x, self.y, self.width,self.height)) 

        text_color = self.text_hover_color if hovering else self.text_color
        screen.blit(self.font.render_text(self.text, text_color), self.font.button_middle(self))


    def mouse_over(self) -> bool:
        mx, my = mouse.get_pos()
        if mx >= self.x and mx <= self.x + self.width:
            if my >= self.y and my <= self.y + self.height:
                return True
        return False
    

