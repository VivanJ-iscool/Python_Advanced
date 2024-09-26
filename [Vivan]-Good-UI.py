from tkinter import *
root=Tk()
f1=Frame(root, height='600', width='600', bg='beige')
f1.pack()

root.title('The best user Interface!')
root.geometry('100x100')
root.resizable(True, True)

get_name = Label(f1, width =50, height=100, text='What is your name?')
answer = StringVar()
name = Entry(f1, bg='light grey', textvariable=answer)
name.pack()
get_name.pack()


var = Int
