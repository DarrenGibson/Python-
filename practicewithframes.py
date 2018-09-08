#==================================================================
#			            Practice With Frames 
#==================================================================

''' 
Date    : Fri 07 Sep 2018 02:12:14 PM PDT 
Subject : Python 
Title   : Practice with frames
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

CRM = Tk()
CRM.geometry('800x800+0+0')
CRM.title('Customer Relations Management System')

frame1= Frame(CRM, width = 800, height = 40, bd = 2, relief='raise')
frame1.pack(side=TOP)

frame1_title=Label(frame1, font=('arial', 5, 'bold'), text='Customer Service Relations Manager', bd=4, anchor='w')
frame1_title.grid(row=0, column=0)

frame2= Frame(CRM, width = 800, height = 40, bd = 2, relief='raise')
frame2.pack(side=TOP)

text_Input=StringVar()
txtDisplay = Entry(frame2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=8, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)

# why does the text sixe make the entire frame smaller 

'''
frame2a= Frame(frame2, width = 40, height = 20, bd = 2, relief='raise')
frame2a.pack(side=TOP)
'''

CRM.mainloop()





























































































