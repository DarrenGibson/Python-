#==================================================================
#			             Virtual cash register
#==================================================================

''' 
Date    : Tue 04 Sep 2018 10:46:15 PM PDT 
Subject : python
Title   : virtual cash register
Source  : https://www.youtube.com/watch?v=sHa827pDvnw&t=70s
''' 

#

'''
NOTES:

'''

# 

from tkinter import*
import time;
import random 
import datetime

root = Tk()
root.geometry('1350x650+0+0')
root.title('Billing System')

Tops = Frame(root, width=1350, height=100, bd=8, relief='raise')
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=650, bd=8, relief='raise')
f2.pack(side=LEFT)

f1a = Frame(f1, width=900, height=330, bd=8, relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, relief='raise')
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=8, relief='raise')
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, relief='raise')
f1ab.pack(side=RIGHT)


f2aa = Frame(f2a, width=450, height=330, bd=8, relief='raise')
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8, relief='raise')
f2ab.pack(side=LEFT)

lblInfo=Label(Tops, font=('arial', 60, 'bold'), text='          Online Billing Systems           ', bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

#==================================================Calculator=================================================#
text_Input=StringVar()

txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)




root.mainloop()










































