# Dictionaries

def spam1():
	myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
	print(myCat['color'])
	print('My cat is the color ' + myCat['color'])
	return 'fat' in myCat

def spam2():
	spam1 = [1,2,3]
	spam2 = [1,3,2]
	return spam1 == spam2

def birthdays():

	birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12','Carol': 'Mar 4'}

	while True:
		name = input('Please input the name you want the birthday for (enter to exit): ')
		if name == '':
			break
		else:
			if name in birthdays:
				print('The birthday of ' + name + ' is ' + birthdays[name])
			else:
				newBirthday = input('That persons birthday is not registred, what is their birthday?: ')
				birthdays[name] = newBirthday
				print('Registred birthdays updated. Go again')

def spam3():
	spam = {'color': 'red', 'age': 42}
	print(list(spam.values())[0])
	for i in spam.values():
		print(i)
	for j in spam.keys():
		print(j)
	for k in spam.items():
		print(k)

def spam4():
	spam = {'name': 'Zophie', 'age': 7}
	return 7 in spam.values()

def spam5():
	picnicItems = {'apples': 5, 'cups': 2}
	print('I am bringing ' + str(picnicItems.get('cups',0)) + ' cups.')
	print('I am bringing ' + str(picnicItems['apples']) + ' apples')

def spam6():
	spam = {'name': 'Pooka', 'age': 5}
	while True:
		answer = input()
		if answer == '':
			break
		else:
			if answer in spam:
				print(spam[answer])
			else:
				new = input('What should it be then?')
				spam[answer] = new

def spam7():
	message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
	count = {}

	for character in message:
		count.setdefault(character,0)
		count[character] = count[character] + 1
	print(count)
	print(count.get('c',0))
	pprint.pprint(count)

def spam8():
	spam = {'size': 'big'}
	if 'color' not in spam:
		spam['color'] = 'black'
	print(spam)

def ticTacToe():

	def board():
		print(' ' + theGame['top-L'] + ' | ' + theGame['top-M'] + ' | ' + theGame['top-R'])
		print('-----------')
		print(' ' + theGame['mid-L'] + ' | ' + theGame['mid-M'] + ' | ' + theGame['mid-R'])
		print('-----------')
		print(' ' + theGame['bot-L'] + ' | ' + theGame['bot-M'] + ' | ' + theGame['bot-R'])


	theGame = {
				'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			   	'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			   	'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
			  }
	turn = 2
	board()
	while True:

		print('Circle starts')
		if turn % 2 == 0:
			piece = 'O'
		else:
			piece = 'X'

		move = input('Which cell do you wish to put in? (top-L, mid-M, bot-R etc): ')
		theGame[move] = piece
		turn += 1

		board()

		if (theGame['top-L'] == 'X' and theGame['top-M'] == 'X' and theGame['top-R'] == 'X') or (theGame['top-L'] == 'O' and theGame['top-M'] == 'O' and theGame['top-R'] == 'O') or (theGame['mid-L'] == 'X' and theGame['mid-M'] == 'X' and theGame['mid-R'] == 'X') or (theGame['mid-L'] == 'O' and theGame['mid-M'] == 'O' and theGame['mid-R'] == 'O') or (theGame['bot-L'] == 'X' and theGame['bot-M'] == 'X' and theGame['bot-R'] == 'X') or (theGame['bot-L'] == 'O' and theGame['bot-M'] == 'O' and theGame['bot-R'] == 'O') or (theGame['bot-R'] == 'X' and theGame['mid-R'] == 'X' and theGame['top-R'] == 'X') or (theGame['bot-R'] == 'O' and theGame['mid-R'] == 'O' and theGame['top-R'] == 'O') or (theGame['bot-M'] == 'X' and theGame['mid-M'] == 'X' and theGame['top-M'] == 'X') or (theGame['bot-M'] == 'O' and theGame['mid-M'] == 'O' and theGame['top-M'] == 'O') or (theGame['bot-L'] == 'X' and theGame['mid-L'] == 'X' and theGame['top-L'] == 'X') or (theGame['bot-L'] == 'O' and theGame['mid-L'] == 'O' and theGame['top-L'] == 'O') or (theGame['bot-L'] == 'X' and theGame['mid-M'] == 'X' and theGame['top-R'] == 'X') or (theGame['bot-L'] == 'O' and theGame['mid-M'] == 'O' and theGame['top-R'] == 'O') or (theGame['bot-R'] == 'X' and theGame['mid-M'] == 'X' and theGame['top-L'] == 'X') or (theGame['bot-R'] == 'O' and theGame['mid-M'] == 'O' and theGame['top-L'] == 'O'):
			print(piece + ' wins')
			again = input('Want to play again? y or n: ')
			if again == 'n':
				break
			else:
				theGame = {
				'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			   	'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			   	'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
			  	}
				continue














