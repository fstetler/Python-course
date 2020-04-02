# Input Validation

def spam1():
	while True:
		age = input('Please input your age: ')
		try:
			age = int(age)
		except:
			print('Please use numeric digits')
			continue
		if age < 1:
			print('Please enter a positive number.')
			continue
		break
	print(f'Your age is {age}.')

import pyinputplus as pyip
def spam2():
	response = pyip.inputNum('Please input a number: ')
	print(response)		

def spam3():
	response = pyip.inputNum('Please enter number: ', limit = 2, default = 'Youve tried too many times')
	print(response)

def spam4():
	response = pyip.inputNum('Please input a number: ', allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
	print(response)

def spam5():
	response = pyip.inputNum('Please input a number: ', blockRegexes = [r'[02468]$'])
	print(response)

def spam6():
	response = pyip.inputStr('Input a word: ', allowRegexes = [r'caterpillar','category'], blockRegexes = [r'cat'])
	print(response)

def addsUpToTen():
	while True:
		numbers = pyip.inputInt('Please input a few numbers, without spacing (like this: 123): ')
		sum = 0
		for i in str(numbers):
			sum = sum + int(i)
		if sum != 10:
			print('The digits must add up to 10, not ' + str(sum))
			continue
		else:
			print('The digits add up to 10, see? ' + str(sum)) 
			break

def addsUpToTen2(numbers):
	numbers = str(numbers)
	numbersList = list(numbers)
	for i, digit in enumerate(numbersList):
		numbersList[i] = int(digit)
	if sum(numbersList) != 10:
		raise Exception('The digits must add up to 10 not %s.' % (sum(numbersList)))
	return int(numbers)

def idiot():
	while True:
		prompt = 'Want to know how to keep an idiot busy for hours? \n'
		response = pyip.inputYesNo(prompt)
		if response == 'no':
			break
	print('Thank you. Have a nice day')











