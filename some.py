#==================================================================
#			             this and that 
#==================================================================

''' 
Date    : Sat 08 Sep 2018 08:34:40 PM PDT 
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

topFrame = Frame(root)
topFrame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Click Here')
button1.grid(row=0, column=0)

button2 = Button(topFrame, text='Click Here')
button2.grid(row=1, column=0)

button3 = Button(topFrame, text='Click Here')
button3.grid(row=2, column=0)

button4 = Button(topFrame, text='Click Here', fg='red')
button4.grid(row=3, column=0)



root.mainloop()




















































































