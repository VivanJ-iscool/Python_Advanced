from tkinter import *
root=Tk()
f1=Frame(root, bg='beige')
root.title('The worst user interface!')
root.geometry('600x600') 
root.resizable(True, True)

get_name = Label(root, width =50, height=100, text='What is your name?')
name = Entry(root, bg='light grey')
get_name.pack()
name.pack()





root.mainloop()
