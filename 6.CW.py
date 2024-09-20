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


#TEXTBOX
textbox = Text(root, width = 50, height = 20, background = 'yellow')
textbox.insert('1.0','here is my default text\n')
words_on_line_1 = textbox.get('1.0', 'end')
print(words_on_line_1)

textbox.grid(row = 1)



#
#to : the ending value on the slider
#tickinterval : the length between ticks along the scale, starting at from_
#resolution : how specific the scrollbar is -
#ex. if from_ is 0 and resolution is 1, user can scroll to 0, 1, 2, 3, 4, …
#ex. if from_ is 10 and resolution is 5, user can scroll to 10, 15, 20, 25, …
#orient : either HORIZONTAL or VERTICAL
#There are other configuration options you can read about in the documentation.


var = IntVar()
scalebar = Scale(root, variable = var, bg = 'red', tickinterval=10,
resolution = 10, orient = HORIZONTAL, from_ = 50, to = 80)
scalebar.grid(row = 2, sticky = 'news')
# To fetch current value use variable var or
current_value = scalebar.get()










root.mainloop()
