# Debugging

def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string.')
	if width <= 2:
		raise Exception('Width must be greater than 2')
	if height <= 2:
		raise Exception('Height must be greater than 2')

	print(symbol * width)
	for i in range(height - 2):
		print(symbol + ('' * (width-2)) + symbol)
	print(symbol*width)

def spam1():

	for sym, w, h in (('*',4,4), ('O',20,5),('x',1,3),('ZZ',3,3)):
		try:
			boxPrint(sym,w,h)
		except Exception as err:
			print('An exception happened: ' + str(err))

def boxTest(a, b, c):
	if a < 2:
		raise Exception('a must be higher than 1')
	if b < 2:
		raise Exception('b must be higher than 1')
	if c < 2:
		raise Exception('c must be higher than 1')

	print(a*b)	
	print(a+c)
	print(b+c)

def boxTestspam():
	for a, b, c in ((3,4,1), (2,4,3), (5,1,1)):
		try:
			boxTest(a,b,c)
		except Exception as err:
			print('An exception happened: ' + str(err))


import traceback
# How to write the error message into a txt into your folder
def spam2():
	try:
		raise Exception('This is the error message')
	except:
		errorFile = open('errorInfo.txt','w')
		errorFile.write(traceback.format_exc())
		errorFile.close()
		print('The traceback info was written to errorInfo.txt')

def spam3():
	ages = [26,57,92,54,22,15,17,80,47,73]
	ages.sort()
	return ages
	
def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'
	assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
	print(stoplight)

import logging
def spam4():
	logging.basicConfig(level=logging.DEBUG, format=' %asctime)s - %(levelname)s - %(message)s')


def factorialLog():
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
	logging.debug('Start of program')

	def factorial(n):
		logging.debug('Start of factorial(%s%%)' % (n))
		total = 1
		for i in range(1,n + 1):
			total *= i
			logging.debug('i is ' + str(i) + ', total is ' + str(total))
		logging.debug('End of factorial(%s%%)' % (n))
		return total
	print(factorial(5))
	logging.debug('End of program')



























