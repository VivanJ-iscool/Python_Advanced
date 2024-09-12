from tkinter import *
root = Tk()
a = IntVar()
f = Frame(root,width=600,height=600,bg = "brown")
f.pack()

# img = PhotoImage(file='4.CW\dawg.png')  <DAWGGGGGG
# l1 = Label(f, image=img)  <DAWGGGGGGGG
# l1.pack()    <DAWGGGGGGG

# l1 = Label(f, text='helloo!', bg='black', fg='blue', justify='center', padx=25, pady=25, font='17')  <HELLOOOOOOOOO!
# l1.pack() <HELLOOOOOOOOOOO!



b = Button(root, text = "click me!")
b.pack()

def print2():
    print("Hellooo")

b2 = Button(root, text = "Prints Hellooo", command = print2, fg = 'red', state = 'active')
b2.pack()


b3 = Checkbutton(root, text = "1+1=2")
b3.pack()



release = StringVar()
# this will tell hold the value for button that was selected
ra = Radiobutton(root, text="Option A",
variable=release, value=0)
rb = Radiobutton(root, text="Option B",
variable=release, value=1)
rp = Radiobutton(root, text="Option C",
variable=release, value=2)



ra.pack()
rb.pack()
rp.pack()


textbox = StringVar()
entrybox = Entry(root, textvariable = textbox)
entrybox.pack()
# 
















root.mainloop()