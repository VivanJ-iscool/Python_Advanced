from tkinter import *
root=Tk()
root.title('The best user Interface!')
root.geometry('600x600')
root.resizable(True, True)
f1=Frame(root, height='600', width='600', bg='beige')


get_name = Label(f1,text='What NPC would you like to be?')
get_name.pack(side=TOP)

scroller = Scrollbar(f1, orient=VERTICAL)
listvar = StringVar(value = ('NPC 1- Name begins with A-E','NPC 2- Name begins with F-L', 'NPC 3-Name begins with M-S', 'NPC 4- Name begins with T-Z'))
listbox = Listbox(f1, listvariable = listvar, height = 3, yscrollcommand=scroller.set)#yscroll command makes it scroll up and down
scroller.config(command= listbox.yview) 
scroller.pack(side = RIGHT, fill = Y)#comes at the right side of the screen, top to bottom
listbox.pack(side = TOP)

birthday = Label(f1, text="What month is your birthday in (1 being january, 2 being february, etc.)?")
birthday.pack(side=TOP)
var = IntVar()
scalebar = Scale(f1, variable = var, bg = 'red', tickinterval=3, resolution = 1, orient = HORIZONTAL, from_ = 1, to = 12)
scalebar.pack()


f1.pack()



root.mainloop()
