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
'''

# ----------------------------------------------------------------------------------------

'''

def dg(name):

	print('name')
	return name
	
print(dg(tommy))

'''


# -----------------------------------------------------------------------------------------


'''




def fun1():
	print('Im func1()     I have      pass                             ')
	

def fun2():
	print('Im func2()     I have      print("hi")                      ')
	print('hi')
	
def fun3():
	print('Im func3()     I have      return "bye"                     ')
	return 'bye'
	
def fun4():
	print('Im func4()     I have      print("hi") & return "bye"       ')
	print('hi')
	return 'bye'


fun1()
fun2()
fun3()
fun4()

print('------------------------------------------------------')

def fun1p():
	print('Im print(func1())     I have      pass                             ')
	

def fun2p():
	print('Im print(func2())     I have      print("hi")                      ')
	print('hi')
	
def fun3p():
	print('Im print(func3())     I have      return "bye"                     ')
	return 'bye'
	
def fun4p():
	print('Im print(func4())     I have      print("hi") & return "bye"       ')
	print('hi')
	return 'bye'

print(fun1p())
print(fun2p())
print(fun3p())
print(fun4p())





****
# this sill/ also displayed none 

def dg():
	print()
	return 

print(dg())







def dg():
	print('upper work?')
	return 'test' 
	
# print(dg())

# we can treat this executed function just like a string
# we can also chain .upper 
	
# print(dg().upper())


# this displayed upper work?, but not capitalized, why?  understand this !
dg().upper()


'''











































































