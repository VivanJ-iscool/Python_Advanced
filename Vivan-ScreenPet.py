'''
Project Name: Screen Pet
Author: Vivan J
Date: 7/09/2024

This intricate project explores the art of animation and creation, using a variety
of shapes. These shapes will make ears, eyes, a nose and more.
'''
#Dependencies(depends on tkinter)
from tkinter import *

#Functions
def print_local_area_cords(event):
    print(event.x, event.y)#for every click in Tkinter window, prints x and y cord in shell

#Root
root = Tk()

#Canvas and drawing/painting
c = Canvas(root, height = 600, width = 600, bg = "yellow")
c.create_rectangle(50, 50, 550, 550, fill = "light blue",tags = ('frame'))
c.create_polygon(210, 285, 175, 200, 260, 225, fill = 'brown',outline = 'black', tags = ('left ear'))
c.create_polygon(175,200, 225,268, 210,285, fill = "white", outline = "black", tags = ("inner left ear"))
c.create_polygon(345,225, 420,190, 385,265, fill = "brown", outline = "black", tags = ("right ear"))
c.create_polygon(395,282, 385,265, 420,190, fill = "white", outline = "black", tags = ("Inner right ear"))
c.create_oval(200, 200, 400, 400, fill = "brown", tags=('head'))
c.create_oval(361,269, 315,318, fill = "white", tags =("right eye"))
c.create_oval(275,315, 235,270, fill = "white", tags = ("left eye"))
c.create_oval(310,340, 285,310, fill = "pink", outline = "black", tags=("nose"))
c.create_line(297,338, 330,355, tags=("right whisker"))
c.create_line(297,338, 265,350, tags=("left whisker"))
c.create_oval(250,313, 273,290, fill="black", tags="left pupil")
c.create_oval(336,313, 316,290, fill="black", tags="right pupil")
c.pack()

#Binding and Calling function
root.bind("<Button-1>", print_local_area_cords)

# Do not remove this line! It keeps your window open while the code is running
root.mainloop()
