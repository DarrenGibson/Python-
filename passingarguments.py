#==================================================================
#			       passing arguments to functions 
#==================================================================

''' 
Date    : Sat 15 Sep 2018 07:03:51 PM PDT 
Subject : Python
Title   : Passing arguments to functions 
Source  : 
''' 

# 

'''
NOTES:

# print(firstFun()), and print(firstFun) displays different results

'''

#

'''
from tkinter import*
mainWindow = Tk()
mainWindow.mainloop()
'''



'''
def firstFun():
	print('this works') 
	return'this is return'

firstFun()
print(firstFun()) # this allows us to print whats in return also
	
firstFun() alone will display "this works", not what is in return 
print(firstFun()) alone will display both statements from print and return
if you remove the return statement it will print this works none

we can chain a method to our print funtion 
	print(firstFun().upper())

'''
	
	
# this function works even with integers in this way

'''
fir_num = ''
sec_num = ''
'''

'''
def getNum():
	fir_num = int(input('please give me the first number: '))
	sec_num = int(input('please give me the second number: '))
	return fir_num, sec_num

def addition(a, b):
	sum_total = a + b
	return sum_total
'''
def gh():
	num1 = int(input('Please enter the first number: '))
	num2 = int(input('Please enter the second number: '))
	return num1, num2

def th(num1, num2):
	return nm + nn

def addition(tot, als):
	return tot + als + 12
	
	
	
print(th(gh()))
	


































































