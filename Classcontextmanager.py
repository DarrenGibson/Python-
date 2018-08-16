#=================================================================#
#					       Context managers
#-----------------------------------------------------------------#

'''
Date		: Thu 16 Aug 2018 11:08:00 AM PDT 
Author		: Darren 
Title		: Context Managers
Resources	: Corey Schafer Python Tutorial: Context Managers - Efficiantly Managing Resources
'''

class Create_New():

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
		
	def __exit__(self, exc_type, exc_val, traceback):
		self.file.close()
		
with Create_New('sample3.py', 'w') as f:
	f.write('testing')
	
print(f.closed)
	
	























