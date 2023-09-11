from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, func, text ,row, col, font, color = 'dark-grey'):
        super().__init__(
            master = parent, 
            text = text,
            command = func,
            corner_radius=STYLING['corner-radious'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text']
            )
        self.grid(row=row, column=col, sticky='NESW')