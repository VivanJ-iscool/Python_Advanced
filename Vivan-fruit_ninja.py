'''
Project: Fruit Ninja
Author: Vivan J
Date: 2024/7/23
'''

from tkinter import *
import random as r

root = Tk()
c = Canvas(root, width=600, height=600, bg='blue')
c.pack()
score = 0
lives = 3

class Fruit():
    # Put __init__ function here
    def __init__(self, x,y, fruit_image):
    
        self.obj = c.create_image(x,y, image = fruit_image)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
        self.move()

    def destroy(self, event):
        global score
        score+=1
        print('Score: ',score)
        c.delete(self.obj)

    def move(self):
        # the canvas is told to move this fruit's Canvas Object 0 units right and 1 unit down
        # change the 0 to a nonzero value to have the fruit move left or right
        # change the 1 to a higher number for it to fall faster
        c.move(self.obj, 0, 2)#first number: change to any non-zero value for left/right  second number: higher it is, faster it falls
        root.after(50, self.move)#higher= less fruits fall/longer fruit cooldown  lower= more fruits/fruit cooldown

class bananas(Fruit):
    img= PhotoImage(file= "3.CW/bananas.png")
    def __init__(self, x,y):
        super().__init__(x,y, bananas.img)

class watermelon(Fruit):
    img= PhotoImage(file= "3.CW/watermelon.png")
    def __init__(self, x,y):
        super().__init__(x,y, watermelon.img)

class coconut(Fruit):
    img= PhotoImage(file= "3.CW/coconut.png")
    def __init__(self, x,y):
        super().__init__(x,y, coconut.img)


'''
Create your Bomb class here.
The __init__ should
- create the bomb's Canvas Object and store it as an instance variable
- copy the given extra lines from the Fruit class comments
Give it a destroy method, but it should instead just
print out 'YOU HIT A BOMB', then quit the game using
'root.quit()' which closes our window.
Copy the move function from Fruit here too since it should also fall down the screen.
''' 
class Bomb():#should be it's own parent class, since it has a different role to play in Fruit Ninja!
    img= PhotoImage(file = "3.CW/bomb.png")
    def __init__(self, x, y):
        self.obj = c.create_image(x, y, image=Bomb.img)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
        self.move()
    
    
    def destroy(self, event):
        global lives
        if lives > 0:
            print("Lives: ",lives)
            lives = lives-1
            c.delete(self.obj)
        else:
            print("YOU HIT A BOMB!")
            root.destroy()

    def move(self):
        c.move(self.obj, 0, 2)
        root.after(100, self.move)

fruits = ["bomb", "watermelon", "coconut", "banana"]
def falling_fruits():
    for i in range(3):
        fruit = r.choice(fruits)
        if fruit == "watermelon":
            watermelon(r.randrange(0,600), r.randrange(0,150))
        elif fruit == "banana":
            bananas(r.randrange(0,600), r.randrange(0,150))
        elif fruit == "bomb":
            Bomb(r.randrange(0,600), r.randrange(0,150))
        elif fruit == "coconut":
            coconut(r.randrange(0,600), r.randrange(0,150))
    
    root.after(2000, falling_fruits)

falling_fruits()

root.mainloop()


# class Bonuses(Fruit):
#     pass
# class Coin():
#    pass