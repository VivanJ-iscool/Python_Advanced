from tkinter import *
import random as r
from tkinter import messagebox
root=Tk()
c=Canvas(root, height=600,width=600, bg='light blue')
a=StringVar


menubar = Menu(root)
menu_file = Menu(menubar) 
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_file.add_command(label='Nothing')
menu_file.add_command(label='Open...')
menu_file.add_command(label='Something')
root.config(menu = menubar) 

class Math_Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Game")

        # Set the number of questions, current question, and correct answers to keep track of the game
        self.num_questions = 8
        self.current_question = 0
        self.correct_answers = 0

        # Create the widgets (GUI components) and generate the first question
        self.create_widget()
        self.generate_questions()
    def generate_questions(self):
        if self.generate_questions==9:
            self.reveal_results()
        else:
            self.num_questions+=1
            num1 = r.randint(1, 1500)
            num2 = r.randint(1, 1500)
            self.correct_result = num1 + num2
            self.question_label.config(text=f"Question {self.current_question}: {num1} + {num2} = ?")
        
    def create_widget(self):
        self.question_label = Label(self.root, text="", font=("Helvetica", 16))
        self.question_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.answer_label=Label(root, text='Your Answer: ')
        self.answer_label.grid(row=3, column=1, columnspan=2, rowspan=1, padx=20, pady=20)
        self.answer_box=Entry(root, textvariable=a)
        self.answer_box.grid(sticky='e', row=3, column=3, rowspan=1, columnspan=2)
        self.submit_butt=Button(root, text="SUBMIT", command=self.check_answer)
        self.submit_butt.grid(row=4, column=2, rowspan=1, columnspan=2, padx=40, pady=40)


    def check_answer(self):
        # Check if the user's answer is correct
        user_answer = self.answer_box.get()
        try:
            user_answer=int(user_answer)
            if user_answer==self.correct_result:
                self.correct_answers+=1
                self.generate_questions()
        except ValueError:
            messagebox.showerror(message="Your answer is incorrect! -1 point")
    
    def reveal_results(self):
        messagebox.showinfo(message="Good Effort! You got"+self.correct_answers +"questions correct out of"+self.num_questions+"total questions!")



if __name__ == "__main__":
    root = Tk()
    app = Math_Game(root)  # Create an instance of the MathGameApp class
    root.mainloop()  # Start the tkinter main event loop





