#Question 4
#Level 1

#Question:
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


if __name__ == '__main__':
	input_str = str(raw_input('Podaj ciag liczb: '))
	l = input_str.split(',')
	print l
	t = tuple(l)
	print t