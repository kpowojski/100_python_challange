#Question 1
#Level 1

#Question:
#Write a program which will find all such numbers which are divisible by 7 but #are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_numbers():
	l = []
	for n in range(2000, 3200):
		if n%7==0 and n%5!=0:
			l.append(str(n))
	return ','.join(l)
	
if __name__ == '__main__':
	print find_numbers()
