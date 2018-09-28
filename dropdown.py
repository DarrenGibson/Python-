#==================================================================
#			             Dropdown Menus
#==================================================================

''' 
Date    : Tue 18 Sep 2018 09:07:21 PM PDT 
Subject : Python
Title   : Dropdown Menus 
Source  : Bukys tk series #9
''' 

# 

'''
NOTES:

'''

from tkinter import*

mW = Tk()

drop_file = Menu(mW) 
mW.config(menu=drop_file)

drop_file_sub = Menu(drop_file)
drop_file.add_cascade(label='file', menu=drop_file_sub)
'''
submenu.add_command(label='new project...', command=do)
submenu.add_command(label='new folder.', command=do)
submenu.add_separator()
submenu.add_command(label='print.', command=do)
'''

mW.mainloop()




















































































