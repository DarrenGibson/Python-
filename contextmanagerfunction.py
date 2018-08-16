#=================================================================#
#			creating a context manager with a function
#-----------------------------------------------------------------#

'''
Date		: Thu 16 Aug 2018 11:20:38 AM PDT 
Author		: Darren 
Title		: Creating a context manager with a function
Resources	: Corey Schafer   Python Tutorial: Context Managers - Efficiantly Managing Resources
'''

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
	f = open(file, mode)
	yield f
	f.close()
	
with open_file('sample4.txt', 'w') as f:
	f.write('hello')
	
print(f.closed)





























