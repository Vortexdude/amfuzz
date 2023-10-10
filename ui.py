from shlex import join
from settings import *
import darkdetect
import customtkinter as ctk
from buttons import Button, NumButton, OperationButton

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

        #data
        self.result_string: str = ctk.StringVar(value='0')
        self.formula_sring: str = ctk.StringVar(value='') #setting the string variable for label
        self.display_nums = []

        # widgets
        self.create_widget()
        self.mainloop() #the mainloop

    def create_widget(self):
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        OutputLabel(self, 1, 'E', result_font, self.result_string)
        OutputLabel(self, 0, 'SE', main_font, self.formula_sring)

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
        Button(
            parent=self,
            func=self.percent,
            text=OPERATORS['percent']['text'],
            row=OPERATORS['percent']['row'],
            col=OPERATORS['percent']['col'],
            font=main_font
        )

        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent=self,
                text=num,
                func=self.num_press,
                row=data['row'],
                col=data['col'],
                font=main_font,
                span=data['span']
            )

        for opetation, data in MATH_POSITIONS.items():
            OperationButton(
                parent=self,
                operation=data['operator'],
                text=data['character'],
                func=self.meth_press,
                row=data['row'],
                col=data['col'],
                font=main_font
            )

    def num_press(self, value):
        self.display_nums.append(str(value))
        self.result_string.set(''.join(self.display_nums))

    def meth_press(self, value):
        # current_number = ''.join(self.)
        pass

    def percent(self):
        print("Getting The Percent")

    def clear(self):
        self.display_nums = []
        self.result_string.set("")


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row = row, sticky=anchor, padx=10)

if __name__ == "__main__":
    Calculator(darkdetect.isDark())
    # Calculator(False)
