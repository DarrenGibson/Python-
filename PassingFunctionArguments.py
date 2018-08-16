#---------------------------------------------------------------------
#                           Practice with functions
#---------------------------------------------------------------------

'''
Date:       08/13/18
Author:     darren
Project:    practice
Resources:  various
'''

# we can make this function work with global variables
# but I would like to pass the arguments from the first
# function to the second



'''
def getinput():
    global num1, num2
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))


def getrange():
    for i in range(num1, num2):
        print('{} is the current number'.format(i))


getinput()
getrange()
'''


def getinput():
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))
    # this is creating and returning a single tuple with
    # two values
    return num1, num2


def getrange(data):
    a, b = data
    for i in range(a, b):
        print('{} is the current number'.format(i))


getrange(getinput())












