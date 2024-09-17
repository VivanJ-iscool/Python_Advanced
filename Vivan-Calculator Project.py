'''
Calculator Builder - Starter Code
Author: Vivan J
Date:

[Project Description]

'''
"""
TODO:
SETUP
1. Draw out your calculator on paper - think about what buttons should be included and how to arrange them
    MUST INCLUDE: 0,1,2,3,4,5,6,7,8,9,+,-,*,/, CLEAR, =, DEL (or DELETE or BACKSPACE)
    OPTIONAL: any buttons you choose, like on OFF button linked to root.quit()
2. From this drawing determine what row and column each button should be placed in
3. Pick out a colour-scheme so that your design is attractive

CODING
1. Create a Label that uses the 'expression' StringVar as its textvariable
2. Customize the CalcButton class so that creating your Buttons is easy and standardized
    2.1 Add more parameters to the __init__ function so your buttons can be created inside it
    2.2 Set the 'command' for your Buttons to be 'self.onClick' so that you can use the premade functions
3. Create a Label that uses the 'expression' StringVar as its textvariable - this is the top of the calculator where the expression appears
4. Create your Buttons using the CalcButton class. Some buttons you may want to create without it, especially if they have special commands.
    4.1 Your '=' button, for example, should have its command set to the 'evaluate' function instead
    4.2 Your 'CLEAR' button should have its command set to the 'clear' function

"""


from tkinter import *
root = Tk()
expression = StringVar()
root.geometry("200x500")
display= Label(root, textvariable=expression)

class CalcButton():
    def __init__(self, char, bg, fg, collumn, row, command=None):  # add extra parameters

        # this should be the character on the button, like '2' or '+' as a one character string
        self.char = char

        if command == None:
            self.onClick()

        self.obj = Button(frame, text=char, command=command, bg=bgcol, fg=fgcol, relief='raised')  # create your Button and store it as the 'obj' instance variable
        self.obj.grid(row=row, column=col, sticky='news')
        # are there any other pieces of information a button should store?

    def onClick(self):
        """
        This function simply adds this buttons character to the expression
        """
        expression.set(expression.get() + self.char)


def clear():
    """
    Clears the expression.
    """
    expression.set('')


def delete():
    """
    Removes the last character in expression.
    """
    expression.set(expression.get()[:-1])


def evaluate():
        # Evaluate the expression using the 'eval' function and update the result
        result = str(eval(expression.get()))
        expression.set(result)
    except Exception:
        # Handle any evaluation errors by displaying "Error"
        expression.set('Error')

# Create your frames and label here
mainframe = Frame(root, bg='light grey', padx=10, pady=15)
mainframe.grid(row, column, rowspan=4, columnspan=4)

display_box = Label(mainframe, bg='white', fg='black', textvariable=expression, justify='right', relief='sunken', width=mainframe.winfo_width())
display_box.grid(row=0, column=0, columnspan=5, sticky='news')

special_BFrame = Frame(mainframe, bg='orange', relief='flat', padx=5, pady=5)
special_BFrame.grid(row=1, column=0, columnspan=4, sticky='ew')

numpad_frame = Frame(mainframe, bg='light grey', padx=5, pady=5, relief='flat')
numpad_frame.grid(row=2, column=0, rowspan=4, columnspan=4, sticky='news')








# Create your buttons here
CalcButton("1","black","orange",0,0, numpad_frame)
CalcButton("2","black","orange",1,0, numpad_frame)
CalcButton("3","black","orange",2,0, numpad_frame)
CalcButton("4","black","orange",0,1, numpad_frame)
CalcButton("5","black","orange",1,1, numpad_frame)
CalcButton("6","black","orange",2,1, numpad_frame)
CalcButton("7","black","orange",0,2, numpad_frame)
CalcButton("8","black","orange",1,2, numpad_frame)
CalcButton("9","black","orange",2,2, numpad_frame)
CalcButton("0","black","orange",1,3, numpad_frame)

CalcButton(numpad_frame, '.', 'orange', 'black', 3, 1)
CalcButton(numpad_frame, '=', 'orange', 'black', 3, 2, command=evaluate)
CalcButton(numpad_frame, '/', 'orange', 'black', 0, 3)
CalcButton(numpad_frame, '*', 'orange', 'black', 1, 3)
CalcButton(numpad_frame, '-', 'orange', 'black', 2, 3)
CalcButton(numpad_frame, '+', 'orange', 'black', 3, 3)

CalcButton(special_BFrame, 'OFF', 'dark grey', 'black', 0, 0, command=root.quit)
CalcButton(special_BFrame, 'CLR', 'dark grey', 'black', 0, 1, command=clear)
CalcButton(special_BFrame, 'DEL', 'dark grey', 'black', 0, 2, command=delete)

# Configure your rows and columns here as needed - remember to configure the root as well as your frames!
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

for i in range(3):
    mainframe.rowconfigure(i, weight=1)
    mainframe.columnconfigure(i, weight=1)

special_BFrame.rowconfigure(0, weight=0)
for i in range(3):
    special_BFrame.columnconfigure(i, weight=1)

for i in range(4):
    numpad_frame.rowconfigure(i, weight=1)
    numpad_frame.columnconfigure(i, weight=1)

root.mainloop()
