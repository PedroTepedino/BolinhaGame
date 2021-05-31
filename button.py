from vector import Vector
from graphics import *


class Button:
    def __init__(self,
                 window: GraphWin,
                 callback,  # function
                 center: Vector,
                 half_size: Vector,
                 text: str,
                 text_size: int = 20,
                 text_outline_color=color_rgb(0, 0, 0),
                 line_color=color_rgb(0, 0, 0),
                 fill_color=color_rgb(255, 255, 255),
                 hover_text_outline_color=color_rgb(255, 255, 255),
                 hover_line_color=color_rgb(255, 255, 255),
                 hover_fill_color=color_rgb(0, 0, 0),
                 ):

        self.window = window

        self.selected = False

        self.center = center
        self.half_size = half_size

        self.callback = callback

        self.hover_fill_color = hover_fill_color
        self.hover_line_color = hover_line_color
        self.hover_text_outline_color = hover_text_outline_color

        self.fill_color = fill_color
        self.line_color = line_color
        self.text_outline_color = text_outline_color

        self.text_size = text_size

        self.square = Rectangle((center + half_size).to_point(), (center - half_size).to_point())

        self.text = Text(center.to_point(), text)
        self.text.setSize(text_size)

        self.reset_graphics()

    def draw(self):
        self.square.draw(self.window)
        self.text.draw(self.window)

    def undraw(self):
        self.square.undraw()
        self.text.undraw()

    def redraw(self):
        self.undraw()
        self.draw()

    def is_mouse_over(self, mouse_position: Vector) -> bool:
        return (self.center.x - self.half_size.x) <= mouse_position.x <= (self.center.x + self.half_size.x) and (self.center.y - self.half_size.y) <= mouse_position.y <= (self.center.y + self.half_size.y)

    def on_hover(self):
        self.square.setFill(self.hover_fill_color)
        self.square.setOutline(self.hover_line_color)
        self.text.setOutline(self.hover_text_outline_color)

    def reset_graphics(self):
        self.square.setOutline(self.line_color)
        self.square.setFill(self.fill_color)
        self.text.setOutline(self.text_outline_color)

    def click(self):
        self.callback()

    def tick(self, mouse_position: Vector, mouse_click_position):
        self.selected = self.is_mouse_over(mouse_position)

        if self.selected:
            self.on_hover()
        else:
            self.reset_graphics()

        if self.selected and mouse_click_position is not None:
            self.click()

