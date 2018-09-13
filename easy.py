#==================================================================
#			            fun with tkinter 
#==================================================================

''' 
Date    : Mon 10 Sep 2018 11:49:40 PM PDT  
Subject : Practice 
Title   : Creating Windows
Source  : Bucky
''' 

# 

'''
NOTES:

'''

from tkinter import*

root = Tk()

fLabel = Label(root, text='')
fLabel.grid(row=0, column=0)
fLabel = Label(root, text='')
fLabel.grid(row=0, column=1)

fLabel = Label(root, text='First name')
fLabel.grid(row=1, column=0)
enter = Entry(root, width=10)
enter.grid(row=1, column=1)
button1 = Button(root, text='Click Here')
button1.grid(row=1, column=2)

fLabel = Label(root, text='Middle name')
fLabel.grid(row=2, column=0)
enter = Entry(root, width=10)
enter.grid(row=2, column=1)
button2 = Button(root, text='Click Here', fg='red')
button2.grid(row=2, column=2)

fLabel = Label(root, text='Last name ')
fLabel.grid(row=3, column=0)
enter = Entry(root, width=10)
enter.grid(row=3, column=1)
button3 = Button(root, text='Click Here', fg='blue')
button3.grid(row=3, column=2)

fLabel = Label(root, text='')
fLabel.grid(row=4, column=0)
fLabel = Label(root, text='')
fLabel.grid(row=4, column=1)

fLabel = Label(root, text='Address ')
fLabel.grid(row=5, column=0)
enter = Entry(root, width=10)
enter.grid(row=5, column=1)
button4 = Button(root, text='Click Here', fg='green')
button4.grid(row=5, column=2)

fLabel = Label(root, text='City ')
fLabel.grid(row=6, column=0)
enter = Entry(root, width=10)
enter.grid(row=6, column=1)
button5 = Button(root, text='Click Here')
button5.grid(row=6, column=2)

fLabel = Label(root, text='State')
fLabel.grid(row=7, column=0)
enter = Entry(root, width=10)
enter.grid(row=7, column=1)
button6 = Button(root, text='Click Here')
button6.grid(row=7, column=2)

fLabel = Label(root, text='Zip Code')
fLabel.grid(row=8, column=0)
enter = Entry(root, width=10)
enter.grid(row=8, column=1)
button7 = Button(root, text='Click Here')
button7.grid(row=8, column=2)

fLabel = Label(root, text='')
fLabel.grid(row=9, column=0)
fLabel = Label(root, text='')
fLabel.grid(row=9, column=1)

fLabel = Label(root, text='Phone ')
fLabel.grid(row=10, column=0)
enter = Entry(root, width=10)
enter.grid(row=10, column=1)
button7 = Button(root, text='Click Here')
button7.grid(row=10, column=2)

fLabel = Label(root, text='Email')
fLabel.grid(row=11, column=0)
enter = Entry(root, width=10)
enter.grid(row=11, column=1)
button8 = Button(root, text='Click Here')
button8.grid(row=11, column=2)

root.mainloop()







































































