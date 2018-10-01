#==================================================================
#			              
#==================================================================

''' 
Date    : Sat 29 Sep 2018 09:39:16 PM PDT 
Subject : Tkinter Python
Title   : creating awesomeness 
Source  : zcheee intranutzz
''' 

# 


'''
NOTES:
# looks like you can pack() in a grid()
'''


from tkinter import *
root = Tk()

##############################   grid 0, 0   ######################################
frame00 = Frame(root)
frame00.grid(row=0, column=0)
labela = Label(frame00, text='Frame 00')
labela.pack()
##############################





##############################   grif 1, 0    ######################################
frame10 = Frame(root)
frame10.grid(row=1, column=0)
labelb = Label(frame10, text='Frame 10')
labelb.pack()
##############################





##############################   grif 0, 1    ######################################
frame01 = Frame(root)
frame01.grid(row=0, column=1)
labelc = Label(frame01, text='Frame 01')
labelc.pack()
##############################





##############################   grif 1, 1    ######################################
frame11 = Frame(root)
frame11.grid(row=1, column=1)
labeld = Label(frame11, text='Frame 11')
labeld.pack()
##############################
















root.mainloop()



















