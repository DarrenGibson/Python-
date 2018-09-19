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

mainWin = Tk()

def do():
	print('this workes')
	
menu1 = Menu(mainWin) 
mainWin.config(menu=menu1)

submenu = Menu(menu1)
menu1.add_cascade(label='file', menu=submenu)
submenu.add_command(label='new project...', command=do)
submenu.add_command(label='new folder.', command=do)
submenu.add_separator()
submenu.add_command(label='print.', command=do)






mainWin.mainloop()




















































































