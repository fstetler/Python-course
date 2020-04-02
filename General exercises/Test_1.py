def checker():
	a = 'Hello'
	b = 'Hello'
	c = 'Goodbye'

	if b == c:
		print('yes')
	else:
		print('no')


def name():
	name = 'Fredrik'
	nameInput = input('Please write in your name')
	while name != nameInput:
		print('Try again')
		nameInput = input('Please write in your name')
	print('Thank you, Fredrik!')

def passwordGuess():
	
	while True:
		print('Who are you?: ')
		name = input()
		if name != 'Fredrik':
			continue
		print('Hello Fredrik, what is the password?: ')
		password = input()
		if password == 'swordfish':
			break
		else:
			continue
	print('Access granted')


def guestNumber():
	name = ''
	while name != 'Fredrik':
		name = input('Please enter your name')
	print('How many guests do you have?')
	numOfGuests = int(input())
	if numOfGuests > 0 and numOfGuests < 10:
		print('You have less than 10 guests')
	elif numOfGuests >= 10:
		print('You have 10 guests or more')

def nameLetterPrinter():
	name = input('Please input your name')
	b = []
	for i in name:
		b.append(i)
	print(b)
	a = ''.join(b)
	print(a)
	print(isinstance(b,str))

def jimmyCounter():
	print('My name is ')
	for i in range(5):
		print('Jimmy Five Times (' + str(i) + ')')

def jimmyCounterWhile():
	print('My name is ')
	i = 0
	while i < 5:
		print('Jimmy Five Times (' + str(i) + ')')
		i = i + 1

def totalAddition():
	total = 0
	for num in range(101):
		total = total + num

	print(total)

def listCreator():
	for i in range(10,5,-1):
		print(i)

def randomListCreator():
	import random
	for i in range(5):
		print(random.randint(-10,5))

def systemExit():
	import sys

	while True:
		print('Type exit to exit')
		exit = input()
		if exit == 'exit':
			sys.exit()
		else:
			continue

def boxes():
	spam = input('Choose between number 1, 2, or 3')
	if spam == '1':
		print('Hello')
	elif spam == '2':
		print('Howdy')
	else:
		print('Greetings!')

def difference():
	for i in range(0,10,1):
		print(i)


def forAndWhile():
	for i in range(1,11):
		print(i)

	n = 1
	while n < 11:
		print(n)
		n = n + 1

def roundAndAbs():
	a = -5.3
	b = abs(a)
	print(b)

def hello(name):
	print('Hello ' + name)
	
def funcCalc(x):
	a = 5
	b = x + a
	print(b)

def getAnswer(answerNumber):
	if answerNumber == 1:
		return '1'
	elif answerNumber == 2:
		return '2'
	elif answerNumber == 3:
		return '3'

def testReturn(x,y):
	a = x + y
	print(a)

def printTest():
	spam = print('Hello!')
	if spam == None:
		return 'yes'
	else:
		return 'no'

def endTest():
	print('Hello', end=' ')
	print('world!')
	print('cats, ', 'dogs, ', 'and mice.')


def spam():
	eggs = 'spam local'
	print(eggs)

def bacon():
	eggs = 'bacon local'
	print(eggs)
	spam()
	print(eggs)

def spam(divideByZero):
	try:
		return 42 / divideByZero
	except ZeroDivisionError:
		print('Error: Zero division')
	
import random, sys
def guessingGame():

	num = random.randint(1,11)
	guessing = True
	guess = int(input('Welcome to the guessing game. Please guess a number between 1 and 10: \n'))
	count = 1
	while guessing:
		if guess != num:
			guess = int(input('Wrong number, guess again!: '))
			count += 1
			print('Youve tried ' + str(count) + ' times')
		elif guess == num:	
			print('You guessed the right number, and it took you ' + str(count) + ' tries!')
			guessing = False

	print('The game is now over.')
	sys.exit()


def listTesting():
	spam = [1,2,3,4,5]
	spam2 = 'shit'
	spamtot = spam+[spam2]
	del spamtot[2]
	print(spamtot)

def catNameGenerator():

	print('Hello cat friend.Please input the name of your cats. Just press enter to end')
	catName = []
	while True:
		print('Input the name of cat number ' + str(len(catName)+1))
		name = input()
		catName = catName + [name]
		if name == '':
			break
	print('The name of your cats are: ')
	for i in catName:
		print(i)


def rangeList():
	animals = ['cat', 'dog', 'fish']
	for i in range(len(animals)):
		#print(i)
		print('Index ' + str(i) + ' has the word ' + animals[i])

def listTrueCheck():
	animals = ['cat', 'dog', 'fish']
	print('dog' in animals)


def myPets():
	petNames = ['Sophie','Jennifer','Ida']
	guessing = True
	while guessing:
		nameGuess = input('Please input a name')

		if nameGuess in petNames:
			print('I have a pet called ' + nameGuess)
			break
		elif nameGuess not in petNames:
			print('I dont have a pet called ' + nameGuess)

	print('Guessing is now over')

def indexCheck():
	animals = ['cow','dog','cat']

	print(animals.index('dog'))

def listAdd():
	animals = ['cow','dog','cat']
	print(animals)
	animals.append('fish')
	print(animals)

def listRemove():
	animals = ['cow','dog','cat']
	print(animals)
	animals.remove(animals[0])
	print(animals)

def sorting():
	numbers = [8,3,4,1,-5,9,1]
	print(numbers)
	numbers.sort()
	print(numbers)
	numbers.sort(reverse=True)
	print(numbers)

import random
def MagicEightBall():
	messages = ['It is certain',
    			'It is decidedly so',
			    'Yes definitely',
			    'Reply hazy try again',
			    'Ask again later',
			    'Concentrate and ask again',
			    'My reply is no',
			    'Outlook not so good',
			    'Very doubtful']

	asking = True
	while asking:
		question = input('Please write a question for the Magic Eight Ball to answer. Question must end with a question mark. Press the N button if you want to quit: ')
		if question == 'n':
			break
		elif question.endswith('?'):
			rand = random.randint(0,len(messages)-1)
			print(messages[rand])
		elif not question.endswith('?'):
			print('The question must end with a question mark')

	print('The game is now over')

def tuples():
	# Tuples lists cannot be changed
	animals = ('dog','cat','cow')
	print(animals)
	print(list(animals))
	print(animals)
	print(list('Hello'))

import copy

def copyTest():
	spam = ['A','B','C','D']
	cheese = copy.copy(spam)
	cheese[1] = 42
	print(spam)
	print(cheese)

def listSummary():
	spam = [2,4,6,8,10]
	#spam.insert(2,'Hello')
	a = spam[int(int('3'*2)//11)]
	print(a)

def dictionaries():
	myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
	print(myCat['size'])

def birthday():

	birthdays = {'Oski': 'April 1', 'Albin': 'June 23'}

	while True:
		person = input('What is the name of the person? Just press enter to quit: ')
		if person == '':
			break

		if person in birthdays:
			print('The birthday of ' + person + ' is ' + birthdays[person])
		if person not in birthdays:
			newBirthday = input('This person is not registred. What is his or her birthday? Press enter to quit: ')
			if newBirthday == '':
				break
			else:
				birthdays[person] = newBirthday

	print('The questions are now over. Goodbye.')

def testMethods():
	spam = {'color': 'red', 'age': '42'}
	for i,k in spam.items():
		print(i)
		print(k)

def testFunction(somevariable):
	x = somevariable + 3
	print(x)

def picnic():
	picnicItems = {'apples': 5, 'cups': 2}
	print('I am bringing ' + str(picnicItems.get('cups',0)) + ' cups')

def picnicTest():
	person = {'Hair': 'red', 'Eyes': 'brown'}
	picnicGear = {'cups': '2', 'plates': '5'}

	while True:	
		choice = input('Write cups for cups and plates for plates: ')
		if choice == 'cups':
			print('There are ' + picnicGear['cups'] + ' number of cups')
		elif choice == 'plates':
			print('There are ' + picnicGear['plates'] + ' number of plates')
		else:
			add = input('That is not registerd. Input the number you have')
			picnicGear[choice] = add
			print(picnicGear)

import pprint
def coldDay():
	message = 'It was a bright cold day in april, and the clocks were striking thirteen.'
	count = {}

	for character in message:
		count.setdefault(character,0)
		count[character] = count[character] + 1

	pprint.pprint(count)

def pprintTest():

	instruments = {'Guitar': 2, 'Piano': 1}
	for i in instruments.items():
		pprint.pprint(i)

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M']	+ '|' + board['top-R'])
	print('--+-+--')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('--+-+--')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def fib():

	a = 1
	b = 1
	fib = [1,1]
	c = []
	number = input('Which fibbonacci number do you want?: ')
	if number == '1':
		print(fib[0])
	elif number == '2':
		print(fib[1])
	else:
		while len(fib) < int(number):
			c = fib[-1] + fib[-2]
			fib.append(c)
		print(fib[-1])

def likes(names):
	print(len(name))
	if int(len(names)) < 1:
		print('no one likes this')
	elif int(len(names)) < 2:
		print(names + ' likes this')
	elif int(len(names)) < 3:
		print(names[0] + ' and ' + names[1] + ' likes this')
	elif int(len(names)) < 4:
		print(names[0] + ', ' + names[1] + ' and ' + names[2] + ' likes this')
	elif int(len(names)) >= 4:
		print(names[0] + ', ' + names[1] + ' and ' + str(len(names[2:])) + ' others like this')

def fibTest():
	num = int(input('Which fib number do you want?: '))
	fib1 = 1
	fib2 = 1
	fib = [fib1, fib2]
	if num == 1:
		print(fib[0])
	elif num == 1:
		print(fib[1])
	elif num > 1:
		while int(len(fib)) < num:
			newFib = fib[-1] + fib[-2]
			fib.append(newFib)
		print(fib)

def find_duplicates(text):
	a = list(text)
	for i in a:#a[a.index(i):
		b = a.remove(i)
		print(b)
	#print(a.index('a'))

import math

def is_square(n):
	
	if n <= 0:
		return False
	if n > 0:
		if n % math.sqrt(n) == 0:
			return True
		else:
			return False

def test1():
	a = ['xoX']
	alist = list(a)
	for i in alist:
		print(i.lower())

def tower_builder(n_floors):
	step = list(range(1,n_floors+1))
	print(step)
	for i in step:
		print(' '*step[n_floors-step[i-1]]  + '*'*(1+(step[i-1]-1)*2))


def numberRank():
	num = 35142
	numList = []
	for i in list(str(num)):
		numList.append(str(i))
	print(numList)
	numList.sort(reverse=True)
	#print(isinstance(numList,str))
	number = ''.join(numList)
	#return int(number)
	print(number)
	#sortList = numList.sort()
	#print(sortList)

def remove_smallest(n):
	return n[:n[n.index(min(n))]] + n[n.index(min(n))+1:]

def shortest_word(s):

	list1 = s.split(' ')
	lenList = []
	for i in list1:
		length = len(i)
		lenList.append(length)
	return lenList[min(lenList)]

import string
def is_program(s):
	s = s.lower()
	letters = string.ascii_lowercase
	lettersInString = []
	b = []
	c = []
	for i in s:
		if i in letters:
			lettersInString.append(i)
	for i in letters:
		if i in lettersInString:
			b = 1
			c.append(b)
		else:
			b = 0
			c.append(b)

	if 0 in c:
		return False
	else:
		return True

def stray(arr):
	arrList = []
	if arr[0] == arr[1]:
		for i in arr:
			if i == arr[0]:
				arrList.append(1)
			else:
				arrList.append(0)
		return arr[arrList.index(0)]
	else:
		if arr[0] == arr[2]:
			return arr[1]
		elif arr[0] == arr[1]:
			return arr[2]
		elif arr[1] == arr[2]:
			return arr[0]

def bouncingBall(h, bounce, window):
	
	if not h > 0 and bounce > 0 and bounce < 1 and window < h:
		return -1

	count = 0
	if h > window:
		count += 1
	else:
		return 0

	h = h*bounce
	while h > window:
		count += 2
		h = h*bounce

	return count

def gimme(input_array):
	
	newInput = sorted(input_array)
	return input_array.index(newInput[1])

def song_decoder(song):
	words = []
	for i in song.split("WUB"):
		if i != '':
			words.append(i)
	return " ".join(words)


def guessingGame2():
	num = random.randint(1,9)
	running = True
	while running:
		guess = int(input('Please guess a number between 1 and 9: '))
		if guess < num:
			print('Thats too low. Guess again')
		elif guess > num:
			print('Thats too high. Guess again. Fucker')
		elif guess == num:
			print('Correct')
			running = False

def high(x):
	wordList = x.split(' ')
	letterList = string.ascii_lowercase
	pointList = []
	sumList = []
	sum = 0
	for i in range(len(letterList)-1):
		pointList.append(i+1)
	for j in wordList:
		for k in j:
			sumList.append(wordList.index(k))
	for l in sumList:
		sum = sum + l
	return sum

import string
def words_to_marks(s):
	lowerLetter = string.ascii_lowercase
	return lowerLetter.index('a')+1

s = 'attitute'
print(words_to_marks(s))