from tkinter import *
# ?ttk 
from tkinter import ttk
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

'''
drop_main = Menu(root)
root.config(menu=drop_main)
drop_main.add_cascade(label='File', menu=drop_main)


# root object 
root = Tk()

# title 
root.title('Firstnot really though, GUI')

# Button 
# ttk command - learn the difference between this and what i have already used 
# this displays nothing until ---1  <---keep this as example 
# here we can just ?chain, a ?method ?to    <---  This to
ttk.Button(root, text='All tkinter widgets ')#.grid()

drop_file = Menu(root) 
root.config(menu=drop_file)

# whatever all this is 
frame = Frame(root)

button = Button(frame, text='click here')
button = Button(frame, text='click here')
button = Button(frame, text='click here')
button = Button(frame, text='click here')
button = Button(frame, text='click here')
button = Button(frame, text='click here')

label_text = StringVar()
label = Label(frame, textvariable=label_text)

label_text.set('Iam a label')

frame.pack()
button.pack()
label.pack()
# gonna need to learn all that

'''














