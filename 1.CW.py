from tkinter import *
root = Tk()
c = Canvas(root, height=600, width=600, bg='light blue')
c.pack()
def print_loc_area_cords(event):
    print(event.x, event.y)

c.create_line(600,0, 0,600)
c.create_line(0,0, 600,600)
c.create_rectangle(10,400, 300,10, fill="red")
c.create_oval(20,390, 250,20, fill="yellow")
c.create_polygon(150,300, 300,150, 30,150, fill="green")

root.bind("<Button-1>", print_loc_area_cords)
root.mainloop()
