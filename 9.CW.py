from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

root=Tk()
# new_window = Toplevel(root)
# new_window.title('Pop Up # 1') # change the title
# current_title = new_window.title() # get the current title
# new_window.geometry('300x200')
# # window will be 300 pixels wide, 200 tall, with top left corner at (5,20)
# new_window.resizable(True, False) # can resize width, not height

# close = messagebox.askokcancel(message='You have a syntax error! (sike)')
# print(close)


menubar = Menu(root) # Create a Menu object
menu_file = Menu(menubar) # Another Menu object, but a child of Menubar
menu_edit = Menu(menubar)
# a 'cascade' is an option along the menu bar
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
# a 'command' is an option in a Menu's dropdown options
menu_file.add_command(label='New')
menu_file.add_command(label='Open...')
menu_file.add_command(label='Close')
root.config(menu = menubar) # Set menubar as the menu attribute of this window!

# open_filename = filedialog.askopenfilename() # 1
# save_filename = filedialog.asksaveasfilename()# 2
# dirname = filedialog.askdirectory()



# rgb, hex = colorchooser.askcolor(initialcolor='#ff0000')
# print(rgb) # RGB representation of selected colour
# print(hex) # HEX code representation of selected colour








root.mainloop()
