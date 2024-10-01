from tkinter import *
root=Tk()
f1=Frame(root, height='600', width='600', bg='beige')

root.title('The best user Interface!')
root.geometry('100x100')
root.resizable(True, True)

get_name = Label(f1, width =50, height=100, text='What is your name?')
answer = StringVar()
name = Entry(f1, bg='light grey', textvariable=answer)
name.pack()
get_name.pack()


var = IntVar()
scalebar = Scale(root, variable = var, bg = 'red', tickinterval=3,
resolution = 1, orient = HORIZONTAL, from_ = 1, to = 12)
scalebar.grid(row = 2, sticky = 'new')
