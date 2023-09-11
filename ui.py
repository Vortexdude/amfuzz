from settings import *
import darkdetect
import customtkinter as ctk
from buttons import Button

class Calculator(ctk.CTk):
    def __init__(self, isdark: bool):

        #initial setup
        super().__init__(fg_color=(WHITE,BLACK))

        # toggle the light nad dark mode using the set appreance mode
        ctk.set_appearance_mode(f'{"dark" if isdark else "light"}')

        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}") # Set the size of the calc
        self.resizable(False, False) # for fixing the position
        self.title(APP_TITLE)
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')
        self.formula_sring: str = ctk.StringVar(value='0') #setting the string variable for label
        self.result_string: str = ctk.StringVar(value='test')

        # widgets
        self.create_widget()
        self.mainloop() #the mainloop

    def create_widget(self):
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        resul_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        OutputLabel(self, 0, 'SE', main_font, self.result_string)
        OutputLabel(self, 1, 'E', resul_font, self.formula_sring)

        # AC button
        Button(
            parent= self,
            func = self.clear,
            text=OPERATORS['clear']['text'],
            row=OPERATORS['clear']['row'],
            col=OPERATORS['clear']['col'],
            font=main_font
        )

        # percent button


    def clear(self):
        print("Clearing the screen !")


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row = row, sticky=anchor, padx=10)

if __name__ == "__main__":
    Calculator(darkdetect.isDark())
    # Calculator(False)
