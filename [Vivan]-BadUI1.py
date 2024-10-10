from tkinter import *
root=Tk()
f1=Frame(root, bg='beige')
root.title('The worst user interface!')
root.geometry('600x600') 
root.resizable(True, True)
realese=StringVar()


get_name = Label(root, text='What is your name?')
get_name.pack()
name1 = Radiobutton(root, bg='light grey', fg='red', text='Shreya', variable=realese, value=0)
name1.pack(side=TOP)
name2 = Radiobutton(root, bg='light grey', fg='red', text='Vivan', variable=realese, value=1)
name2.pack(side=TOP)
name3 = Radiobutton(root, bg='light grey', fg='red', text='Bad Jiya', variable=realese, value=2)
name3.pack(side=TOP)
name4 = Radiobutton(root, bg='light grey', fg='red', text='Killer Parmansh', variable=realese, value=3)
name4.pack(side=TOP)
name5 = Radiobutton(root, bg='light grey', fg='red', text='FEIN', variable=realese, value=4)
name5.pack(side=TOP)


birthmonth=Label(root, text='What is your zodiac?', fg='orange', bg='green')
birthmonth.pack(side=TOP)
txtbox = Text(root, width = 20, height = 10, background='light blue')
txtbox.pack(side=TOP)
txtbox.insert('2.0 -6 chars', 'gemenai')



root.mainloop()
