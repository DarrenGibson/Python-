#==================================================================
#			             Bills 
#==================================================================

''' 
Date    : Thu 27 Sep 2018 04:01:59 PM PDT 
Subject : Personal accounting 
Title   : Bills 
Source  : Various, tkinter 
''' 

# 

'''
NOTES:

'''

# 

from tkinter import *

def do():
	print('say something')

root = Tk()

drop_file = Menu(root) 
root.config(menu=drop_file)

drop_edit = Menu(root) 
root.config(menu=drop_edit)

drop_file_sub = Menu(drop_file)
drop_file_sub.add_command(label='Open', command=do)

drop_file.add_cascade(label='File', menu=drop_file_sub)
drop_edit.add_cascade(label='File', menu=drop_edit)
drop_file.add_cascade(label='Edit', menu=drop_file_sub)
drop_file.add_cascade(label='View', menu=drop_file_sub)




root.mainloop()













































































