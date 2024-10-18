#EVENTS AND BINDING
from tkinter import *
root=Tk()
num = IntVar()

def add():
    num.set(num.get() + 1)
# num.get() gets the current value, num.set() will set the value

desc_label = Label(root, text = 'How many clicks: ', bg = 'blue', fg = 'white')
num_label = Label(root, textvariable=num, bg = 'blue', fg = 'white')
clicker = Button(root, text = 'CLICK ME', bg = 'blue', fg = 'white', command = add) # see how command is set

desc_label.pack(side = TOP, fill = X)
num_label.pack(side = TOP, fill = X)
clicker.pack(side = BOTTOM, fill = X)


# posvar=StringVar

# def update_pos(event):
#     #takes parameter 'event' containing info about the event
#     posvar.set('(%d, %d)'%(round(event.x), round(event.y)))
#     #updates the posvar variable


# loc_label = Label(root, textvariable=posvar, bg='grey', justify='center')
# loc_label.pack(fill=X)

# f=Frame(root, width=400, height=400, bg='white')
# f.pack(side=BOTTOM)

# f.bind('<Motion>', update_pos)





















root.mainloop()