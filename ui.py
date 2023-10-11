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
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='') #setting the string variable for label
        self.display_nums = []
        self.full_operation = []

        # widgets
        self.create_widget()
        self.mainloop() #the mainloop

    def create_widget(self):
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        OutputLabel(self, 1, 'E', result_font, self.result_string)
        OutputLabel(self, 0, 'SE', main_font, self.formula_string)

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
                func=self.math_press,
                row=data['row'],
                col=data['col'],
                font=main_font
            )

    def num_press(self, value):
        self.display_nums.append(str(value))
        self.result_string.set(''.join(self.display_nums))

    def math_press(self, value):
        current_number = ''.join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)
            if value != '=':
                self.full_operation.append(value)
                # clear the number list that hold the previous numbers so it will add the new numbers inthe lsit and add operation
                # example here is 
                '''
                    # display_nums = 12
                    # full_operation = [12, +]
                    # now if you press the bymber again it will give the 
                    # full_operation = [12, +, 12, +, 13] note - here the (12 + ) appears 
                    # again so we need to clear the previous data
                
                '''
                self.display_nums.clear() 
                self.result_string.set("")
                self.formula_string.set(str(' '.join(self.full_operation)))
            else:
                formula = " ".join(self.full_operation)
                result = eval(formula)
                
                # Check the vlaue if float
                if isinstance(result, float):

                    # if the value is like int 4.0 or 1.0 then convert it to 4 or 1
                    if result.is_integer():
                        result = int(result)
                    else:
                        # convert the result upto the limit of 3
                        result = round(result, 3)

                # clear the full operation list
                self.full_operation.clear()
                self.display_nums = [str(result)]

                # update the ouput
                self.result_string.set(result)
                self.formula_string.set(formula)

    def percent(self):
        print("Getting The Percent")

    def clear(self):
        self.display_nums.clear()
        self.full_operation.clear()
        self.result_string.set(0)
        self.formula_string.set("")


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row = row, sticky=anchor, padx=10)

if __name__ == "__main__":
    Calculator(darkdetect.isDark())
    # Calculator(False)
