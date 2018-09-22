#==================================================================
#			             Functions 
#==================================================================

''' 
Date    : Sat 22 Sep 2018 01:56:14 PM PDT 
Subject : Python	
Title   : Functions 
Source  : Corey Shafer 
''' 

# 

'''
NOTES:

'''

def saySomething():
	print('Hello everyone')
	
# print(saySomething())     displays:   none	
#	this is because print is asking for the return value of saySomething

# this will display         displays:   Hello everyone
saySomething()


def saySomethingElse():
	print('other words')
	return 'different words'

saySomethingElse()

# once again, if we did not have a return value it would display none, 
# but we do return 'different words' so it displays that
print(saySomethingElse())














































































