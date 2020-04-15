# Chapter 3

import time, sys
def zigzag():
	indent = 0
	indentIncreasing = True

	try:
		while True:
			print(' '*indent,end='')
			print('********')
			time.sleep(0.1)


			if indentIncreasing:
				indent = indent + 1
				if indent == 20:
					indentIncreasing = False
			else:
				indent = indent - 1
				if indent == 0:
					indentIncreasing = True
	except KeyboardInterrupt:
		sys.exit()

def collatz():
	
	number = int(input('Please input a number: '))
	print(number)
	
	c = 0
	while True:

		if number % 2 == 0:
			c = number // 2
		else:
			c = 3*number + 1
		number = c

		print(number)

		if c == 1:
			break



