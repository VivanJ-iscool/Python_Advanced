'''
Paint App Project
Author: Vivan J
Date: Nov.5th, 2024

[Project Description]
 
'''

from tkinter import *
from tkinter import colorchooser
''''
Your window has been created for you.
TODO:
- create your frame
- create your canvas

'''
root = Tk()
root.title('Paint: Untitled Canvas')
f=Frame(root)
f.pack()
c=Canvas(root, bg="white" ,width=1000, height=1000)
c.pack()

'''
This project will use some global variables.
COLOUR represents the current colour being used, and
SIZE is the current size of the paintbrush.
'''
COLOUR = 'black'
SIZE = 10

class ColourButton():
     '''
     A ColourButton is the class for the buttons at the
     top of the screen that change the brush colour.
     '''
     def __init__(self, colour):
          '''
          This is the function called when creating a ColourButton.
          TODO:
          - fill in the line indicated below.
          '''
          self.colour = colour
          self.Button = Button(f, bg=colour, command=self.update)
     
     def update(self):
          '''
          This is the method that is the command for a ColourButton.

          When a ColourButton is pressed, it must ONLY change the global COLOUR
          variable to be this ColourButton's colour attribute/
          TODO:
          - fill in this function. It should be 2 lines.
          '''
          global COLOUR
          COLOUR = self.colour
     
def draw_circle(event):
    '''
    This function is called whenever the user is dragging their mouse on the
    canvas. Use the canvas method 'createoval' to draw a circle there.
    Remember to refer to your global variables to draw the correct circle.
    TODO:
    - finish this function (should be 1-2 lines)
    '''
    c.create_oval(event.x,event.y, event.x + SIZE.get(),event.y + SIZE.get(), fill=COLOUR, outline=COLOUR, tags=[COLOUR])


def clear_canvas():
    '''
    This function is called whent the user presses the CLEAR button.
    It must clear all drawings from the canvas.
    TODO:
    - finish this function (1 line)
    '''
    c.delete("all")
#################### MAIN CODE #########################

'''
Here we first are making the ColourButtons. We will do this in a quick
and expandable way using a list. Add all the colours you want buttons for
to the list 'colours'.
The for loop will create the ColourButton objects.
TODO:
- add at least 4 more colours to the colours list
'''
def color_change():
    rgb, hex = colorchooser.askcolor(initialcolor='#ff0000')
    global COLOUR
    COLOUR = hex


colours = ['red','orange','yellow','green','blue','purple','pink','brown','grey','black']
change_colour= Button(f, bg='orange', fg='black', text='Change Color', command=color_change)
change_colour.grid(row=0, column=4)






 
# for i in range(len(colours)):
#     x = ColourButton(colours[i])
#     x.Button.grid(row=0, column=i)


'''
Next create the CLEAR button and the width slider.

TODO:
- complete the code fragments below
'''
clear_button = Button(f, bg='light grey', fg='black', text="CLR", command=clear_canvas)
clear_button.grid(row = 0, column = 1)

SIZE = IntVar() # We are using the global variable as the int var so it is always updated
scalebar = Scale(f, variable=SIZE, bg='red', tickinterval=1, from_=1, to=10, resolution=1, orient=HORIZONTAL)
scalebar.grid(row = 0, column = 2)

c.bind('<B1-Motion>', draw_circle)
root.bind('<q>', quit)
root.mainloop()

'''
^^^TODO:^^^
- bind the event of mouse button held down while moving ON THE CANVAS to the draw_circle function
- bind the letter q to quitting the program
- mainloop!
'''