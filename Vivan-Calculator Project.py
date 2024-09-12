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
display= Label(root, textvariable=expression)

class CalcButton():
    def __init__(self, char, bg, fg, collumn, row, command=None):  # add extra parameters

        # this should be the character on the button, like '2' or '+' as a one character string
        self.char = char

        if command == None:
            self.onClick()

        self.obj = Button()  # create your Button and store it as the 'obj' instance variable

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
    """
    Calls the built-in function 'eval' which will evaluate a string according to Pythons evauation rules.
    Replaces the existing expression with the result of evaluating the expression.
    strip() removes any trailing whitespace (spaces or newline characters) since eval does not like them.
    Examples:
    eval('3+4') -> '7'
    eval('3 - 3 + 3 + 56') -> '59'              # spaces between numbers are optional
    eval('-2 * 6') -> '-12'                     # do not use 'x' for multiplication, must be '*'
    """
    expression.set(str(eval(expression.get().strip())))

# Create your frames and label here












# Create your buttons here
CalcButton("1","black","orange",0,0)
CalcButton("2","black","orange",1,0)
CalcButton("3","black","orange",2,0)
CalcButton("4","black","orange",0,1)
CalcButton("5","black","orange",1,1)
CalcButton("6","black","orange",2,1)
CalcButton("7","black","orange",0,2)
CalcButton("8","black","orange",1,2)
CalcButton("9","black","orange",2,2)
CalcButton("0","black","orange",1,3)
CalcButton("+", "orange", "black", )

# Configure your rows and columns here as needed - remember to configure the root as well as your frames!


root.mainloop()
