from tkinter import *
root=Tk()
f1=Frame(root, height='600', width='600', bg='beige')

#LIST BOX OF ITEMS
listvar=StringVar(value=('Pizza', 'Oreos', 'Dosa', 'Rice'))
listboxz=Listbox(root, listvariable=listvar, height=5, selectmode='extended')
listboxz.pack()

listboxz.curselection() #turns to buttons to select
listboxz.config(state = 'disabled') #makes it impossible to select items


#SCROLL BAR

# Setup
scroller = Scrollbar(root, orient=VERTICAL)
listvar = StringVar(value = (0,1,2,3,4,5,6,7,8,9,10))
listbox = Listbox(root, listvariable = listvar, height = 3, yscrollcommand=scroller.set)#yscroll command makes it scroll up and down
scroller.config(command= listbox.yview) 


# Screen Placement Using Pack
scroller.pack(side = RIGHT, fill = Y)#comes at the right side of the screen, top to bottom
listbox.pack(side = BOTTOM)









root.mainloop()
