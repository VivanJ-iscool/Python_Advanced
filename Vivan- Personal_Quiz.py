

'''
Project Title: Personal Quiz
Author: Vivan J
Date: Aug 13,2024

[insert description of project and instructions for use]

'''

'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''


from tkinter import *
root = Tk()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []

result = StringVar()
def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

def set_10():
    stringvars[3].set('10')

def set_13():
    stringvars[3].set('13') 

def set_15():
    stringvars[3].set('15')

# Add all your questions and widgets here
#1
f1=Frame(root, bg="light blue")
q1 = Label(f1, bg='light blue', fg='blue', text="What type of data would you need for decimals in python?" )
q1.pack()
g1 = StringVar()
t1 = Entry(f1,fg='blue', textvariable=g1)
t1.pack()
f1.pack()
answers.append('float')
stringvars.append(g1)

#2
f2 = Frame(root, bg="beige")
q2 = Label(f2, bg="beige", fg='purple', text="What's the datatype for the following:  '12.45' ")
q2.pack()
g2= StringVar()
r1 = Radiobutton(f2, bg='beige', fg='purple', text='float', variable=g2, value="float")
r1.pack()
r2 = Radiobutton(f2, bg='beige', fg='purple', text='string', variable=g2, value="string")
r2.pack()
r3 = Radiobutton(f2, bg='beige', fg='purple', text='integer', variable=g2, value="integer")
r3.pack()
f2.pack()
answers.append('string')
stringvars.append(g2)

#3
f3 = Frame(root, bg='pink')
q3 = Label(f3, bg='pink', fg='red', text="what do lists store?")
q3.pack()
g31= StringVar()
g32= StringVar()
g33= StringVar()
cb1 = Checkbutton(f3, bg='pink', fg='red', text="strings, floats, ints, variables, boleans", variable=g31, onvalue="strings, floats, ints, variables, boleans", offvalue='0')
cb1.pack()
cb2 = Checkbutton(f3, bg='pink', fg='red', text="for loops, while loops, nested loops", variable=g32, onvalue="for loops, while loops, nested loops", offvalue='0')
cb2.pack()
cb3 = Checkbutton(f3, bg='pink', fg='red', text="classes, buttons, widgets", variable=g33, onvalue="classes, buttons, widgets", offvalue='0')
cb3.pack()
f3.pack()
answers.append("strings, floats, ints, variables, boleans")
stringvars.append(g31)

#4
f4 = Frame(root, bg='purple')
q4 = Label(f4, bg='purple', fg='cyan', text='How many provinces and territories are there in Canada?')
q4.pack()
f4.pack()
g4= StringVar()
b1= Button(f4, bg='purple', fg='cyan', text='10', state='normal', command=set_10)
b2= Button(f4, bg='purple', fg='cyan', text='13', state='normal', command=set_13)
b3= Button(f4, bg='purple', fg='cyan', text='15', state='normal', command=set_15)
b1.pack()
b2.pack()
b3.pack()
answers.append('13')
stringvars.append(g4)

#5
f5 = Frame(root, bg='black')
q5 = Label(f5, bg='black', fg='orange', text='Who has the sharingan in Naruto')
f5.pack()
q5.pack()
g5= StringVar()
ra1 = Radiobutton(f5, bg='black', fg='orange', text='Naruto', variable=g5, value="Naruto")
ra1.pack()
ra2 = Radiobutton(f5, bg='black', fg='orange', text='Rock Lee', variable=g5, value="Rock Lee")
ra2.pack()
ra3 = Radiobutton(f5, bg='black', fg='orange', text='Sasuke', variable=g5, value="Sasuke")
ra3.pack()
f5.pack()
answers.append('Sasuke')
stringvars.append(g5)






# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!
t= Label(root, text='Score:')
t.pack()
results = Label(root, textvariable=result)
results.pack()

root.mainloop()
