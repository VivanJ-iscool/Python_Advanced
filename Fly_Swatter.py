from tkinter import *
from random import randrange

root = Tk()
c =Canvas(root, width=600, height=600, bg='beige')
c.pack()

class Bug():
    def __init__ (self, x, y, bug_image):
        self.x = x
        self.y = y
        self.obj = c.create_image(x,y, image = bug_image)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)

    def destroy(self, event): 
        c.delete(self.obj)
        print('Got one!')

class Fly(Bug):
    img = PhotoImage(file = "D:\\coding\\Python Advanced (HEE HEE-)\\3.CW\\small_fly.png")
    def __init__(self, x,y):
        super().__init__(x,y, Fly.img)
        
class Ladybug(Bug):
    img = PhotoImage(file = "D:\\coding\\Python Advanced (HEE HEE-)\\3.CW\\small_ladybug.png")
    def __init__(self, x,y):
        super().__init__(x,y, Ladybug.img)

for i in range(10):
    Fly(randrange(0,600), randrange(0,600))
    Ladybug(randrange(0,600), randrange(0,600))

root.mainloop()