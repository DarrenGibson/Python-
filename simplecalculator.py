#==================================================================
#						  Simplecalculator
#==================================================================

''' 
Date :		08/12/18
project:	Simple Calculator
Title:		Simple Caculator by Making Functions 		
source:		https://www.programiz.com/python-programming/examples/calculator
''' 

def addition(a, z):
	return a + z
	
def subtraction(a, z):
	return a - z
	
def multiplication(a, z):
	return a * z 
	
def division(a, z):
	return a / b
	
for i in range (1, 100):
	a = int(input('Please enter a number:'))
	operator = input('PLease choose either ( + - * /)')
	z = int(input('Please enter a number:'))

	if operator == '+':
		print(addition(a, z))
	
	if operator == '-':
		print(subtraction(a, z))

	if operator == '*':
		print(multiplication(a, z))
	
	if operator == '/':
		print(division(a, z))







