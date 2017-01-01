#Question 5
#Level 1

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.



class String:
	
	def __init__(self):
		self.str = ''
	
	def get_string(self):
		self.str = raw_input("Pass string")
		
	def print_string(self):
		print self.str.upper()

		
if __name__ == '__main__':
	str = String()
	str.get_string()
	str.print_string()
