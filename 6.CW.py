from tkinter import *
root=Tk()
f1=Frame(root, height='600', width='600', bg='beige')

listvar=StringVar(value=('Pizza', 'Oreos', 'Dosa', 'Rice'))
listboxz=Listbox(root, listvariable=listvar, height=5, selectmode='extended')
listboxz.pack()



listboxz.curselection()

root.mainloop()