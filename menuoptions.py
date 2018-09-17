


from tkinter import *


mainWindow = Tk()


'''
class DarrensButtons:

    def __init__ (self, f_name, l_name)
        f_name = self.
        l_name = self.

    def saySomthing(self):

'''

def doNothing():
    print('this is awesome')

dropMenu = Menu(mainWindow)
mainWindow.config(menu=dropMenu)

subDropMenu = Menu(dropMenu)
dropMenu.add_cascade(label='File', menu=subDropMenu)
subDropMenu.add_command(label='new project...', command=doNothing)
subDropMenu.add_separator()
subDropMenu.add_command(label='Exit', command=doNothing)

editMenu = Menu(dropMenu)
dropMenu.add_cascade(label='Exit', menu=editMenu)
editMenu.add_command(label='Redo', command=doNothing)

mainWindow.mainloop()





































