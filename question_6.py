#Question 6
#Level 2

#Question:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

from math import sqrt

class Calculation:
	def __init__(self):
		self.C = 50
		self.H = 30
		self.D = None
		self.value = list()
	
	def main(self):
		self.read_D_value()
		for d in self.D:
			self.value.append(self.calc(d))
			#print d
		return ','.join(self.value)
		
		
	def read_D_value(self):
		self.D = raw_input('Pass D values: ').split(',')
		
	def calc(self, d):
		return str(int(sqrt(2*self.C * int(d) / self.H)))
		

if __name__ == '__main__':
	calculation = Calculation()
	result = calculation.main()
	print result