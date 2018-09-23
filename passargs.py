#==================================================================
#			             passing args
#==================================================================

''' 
Date    : Sat 22 Sep 2018 03:15:32 PM PDT 
Subject : Python
Title   : Passing args in functions 
Source  : corey shafer
''' 

# 

'''
NOTES:

We can swap the position of def and reply statements, but print(say(reply must remain last.

having reply fisrt makes more sense because that is the flow of the program 

this accepts an entire string of words 

'''

#simplest idea 
reply = input('type some word(s)')

#creating function that will take and argument and keep it as a variable named word
def say(word):
	# will return whatever value is in word
	return word

# asking the function say to print its return value after accepting the value or reply 
print(say(reply))
	
















































































