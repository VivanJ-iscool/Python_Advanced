#New: pack parameters
from tkinter import *
root= Tk()
f1= Frame(root, width='600', height='600', bg='light blue')

###Side- makes the widget go to a certain place, towards the right, left, top or bottom of your screen
###Expand- makes it so when you expand Tkintner window, the  widget accordingly increases in size, making it luffy when he eats the gum gum fruit
###fill makes it expand depending on if its x or y. x makes it expand left or right and y makes it expand top to bottom 

b1=Button(root, bg='green', fg='black', text='$Click for free money$')
b1.pack(side= LEFT, expand=FALSE, fill=X)
b3=Button(root, bg='green', fg='black', text='$Click for free money$')
b3.pack(side= RIGHT, expand=True, fill=X)
b2=Button(root, bg='green', fg='black', text='$Click for free money$')
b2.pack(side= TOP, expand=FALSE, fill=Y)


#New: Grid parameters

#NARUTO ON TOP
# b4= Button(root,bg='orange', fg='black', text='Naruto OnTop')
# b4.grid(row = 0, column = 0, columnspan= 1, rowspan=1, sticky = 'news')
# b5= Button(root,bg='orange', fg='black', text='Sasuke OnTop')
# b5.grid(row = 0, column = 1, columnspan= 1, rowspan=1, sticky = 'news')
# b6= Button(root,bg='orange', fg='black', text='Kakashi Ontop')
# b6.grid(row = 0, column = 2, columnspan= 1, rowspan=1, sticky = 'news')
# b7= Button(root,bg='orange', fg='black', text='RockLee OnTop')
# b7.grid(row = 1, column = 0, columnspan= 1, rowspan=1, sticky = 'news')
# b8= Button(root,bg='orange', fg='black', text='L Sakura')
# b8.grid(row = 1, column = 1, columnspan= 1, rowspan=1, sticky = 'news')
# b9= Button(root,bg='orange', fg='black', text='Neji OnTop')
# b9.grid(row = 1, column = 2, columnspan= 1, rowspan=1, sticky = 'news')
# b10= Button(root,bg='orange', fg='black', text='Choji OnTop')
# b10.grid(row = 2, column = 0, columnspan= 1, rowspan=1, sticky = 'news')
# b11= Button(root,bg='orange', fg='black', text='Kiba-Akamaru OnTop')
# b11.grid(row = 2, column = 1, columnspan= 1, rowspan=1, sticky = 'news')
# b12= Button(root,bg='orange', fg='black', text='Guy Sensai OnTop')
# b12.grid(row=2, column=2, columnspan=1, rowspan=1, sticky='news')


# #Details of size when expanding window:

# root.rowconfigure(0,weight=2)#specific row changes when sizing the window
# root.rowconfigure(1,weight=2)
# root.rowconfigure(2,weight=2)
# root.columnconfigure(0,weight=2)#specific column changes when sizing the window
# root.columnconfigure(1,weight=2)
# root.columnconfigure(2,weight=2)


#Practice:
# title = Label(root, bg = 'black', fg = 'white', text = 'Title')
# title.grid(row = 0, column = 0, columnspan= 4, sticky = 'ew')
# b1 = Button(root, bg = 'red', fg = 'white', text = 'Left Button')
# b2 = Button(root, bg = 'green', fg = 'white', text = 'Very Very Long Text Button')
# b3 = Button(root, bg = 'blue', fg = 'white', text = 'Right Button')
# b1.grid(row = 1, column = 0, sticky = 'ew')
# b2.grid(row = 1, column = 1, sticky = 'w')
# b3.grid(row = 1, column = 2, sticky = 'w')
# root.rowconfigure(0, weight = 1)
# root.columnconfigure(0, weight = 2)










































root.mainloop()