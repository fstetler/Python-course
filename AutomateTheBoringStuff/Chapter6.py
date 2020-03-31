# Manipulating strings

def spam1():
	spam = "That is Alice's cat"
	print(spam)

def spam2():
	spam = 'That is Alice\'s cat'
	print(spam)

def spam3():
	spam = r'That is Alice\'s cat'
	print(spam)

def spam4():
	spam = '''Dear shithead,

					Thanks'''
	print(spam)

def spam5():
	spam = 'Hello, world'
	fizz = spam[:5]
	print(fizz)

def spam6():
	spam = 'Hello, world!'
	return 'h'.upper() in spam

def spam7():
	one = 'General Kenobi'
	two = 'Surprise'
	print('Hello there!')
	print('Aah, %s, what a pleasant %s' % (one, two))

def spam8():
	feeling = input('How are you? \n')
	if feeling.lower() == 'great':
		print('I feel great too')
	else:
		print('Hope the rest of the day is good')

def spam9():
	spam = 'hello, world!'
	return spam.islower()

def spam10():
	spam = 'hellothere'
	return 'hello'.isalpha() # Only letters, no blanks
	return 'hello123'.isalnum() # Only letters and num, no blanks
	return '123'.isdecimal() # Only of numeric characters, no blanks
	return '   '.isspace() # Only if only spaces, tabs, and newlines, no blanks
	return 'This Is Title 123'.istitle() # Only if words with first uppercase letter followed by lower

def spam11():
	while True:
		age = input('Please enter your age: ')
		if not age.isdecimal():
			print('You need to input a number')
		else:
			break
	while True:
		password = input('Please choose a password of numbers and letters: ')
		if not password.isalnum():
			print('You need to pick a password of only numbers and letters')
		else:
			print('Your age is ' + age + ' and your password is ' + password)
			break

def spam12():
	return 'Hello, world!'.startswith('Hello')
	#return '123'.endswith('23')

def spam13():
	spam = ['cats','rats','elephants','bats']
	new = ', '.join(spam[:-1])
	new = new + ', and ' + spam[-1]
	print(new)

def spam14():
	spam = 'My name is Fredrik'
	print(spam.split(' '))
	print(spam.split('e'))

def spam15():
	before, sep, after = 'Hello, world!'.partition(' ')
	print(before)

def spam16():
	hello = 'Hello'.rjust(20)
	print(hello)
	print('Hello'.rjust(20,'*'))

def spam17():
	picnic = {'apples': 2, 'cups': 3}
	print('Im bringingn ' + str(picnic['cups']) + ' cups and ' + str(picnic.get('mugs',0)) + ' mugs')

def spam18():
	spam = '    Hello, world  '
	print(spam.strip())

def spam19():
	print(ord('B'))
	print(chr(44))

def spam20():
	TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
			'busy': """Sorry, can we do this later this week or next week?""",
			'upsell': """Would you consider making this a monthly donation?"""}

def PigLatin():
	vowels = ['a','e','i','o','u','y']

	sentence = input('Please enter a sentence: ')


	wordList = sentence.split()
	print(wordList)
	newWordList = []

	for i in wordList:
		if len(i) > 1:
			if i[-1] == '.':
				i = i[:-1]
				if i.isalpha():
					if i[0] not in vowels and i[1] not in vowels:
						newWordList.append(i[2:] + i[0:2] + 'ay.')
					elif i[0] not in vowels:
						newWordList.append(i[1:] + i[0] + 'ay.')
					elif i[0] in vowels:
						newWordList.append(i+'yay.')
				else:
					newWordList.append(i + '.')

			else:
				if i.isalpha():

					if i[0] not in vowels and i[1] not in vowels:
						newWordList.append(i[2:] + i[0:2] + 'ay')
					elif i[0] not in vowels:
						newWordList.append(i[1:] + i[0] + 'ay')
					elif i[0] in vowels:
						newWordList.append(i+'yay')
				else:
					newWordList.append(i)
		else:
			newWordList.append(i + 'yay')
	print(' '.join(newWordList))






















