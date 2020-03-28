# Lists

def spam1():
	spam = ['cat','dog','fuck']
	print(spam)

def spam2():
	spam = ['cat','dog','fuck']
	print(spam[1])
	print(isinstance(spam[1],str))
	print('Hello, ' + spam[1])

def spam3():
	spam = [['cat','dog'],[1,2,3,4]]
	print(spam[0][1])

def spam4():
	spam = [['cat','dog'],[1,2,3,4]]
	print(spam[0][-2])

def spam5():
	spam = [1,2,3,4,5]
	print(spam[-1::-2])

def spam6():
	global spam
	spam = ['cat','dog','fuck']
	return len(spam)

def spam7():
	spam = ['cat','dog','fuck']
	spam[0] = 'hello'
	print(spam)

def spam8():
	spam = ['cat','dog','fuck']
	spam = spam + [1,2,3]
	spam[1] = 'hello'
	print(spam)

def spam9():
	spam = ['cat','dog','horse','rat','mouse']
	del spam[0]
	spam.insert(len(spam),'hello')
	print(spam)

def testAppend():
	b = []
	while True:

		answer = input()
		b.append(answer)
		print(b)

def allMyCats():
	running = True
	print('Please input the names of your cats')
	catNames = []
	while running:
		answer = str(input())
		if answer == '':
			break
		else:
			catNames.append(answer)
	print('Your cats names are: \n ')
	for i in catNames:
		print(i)

def spam10():
	for i in range(4):
		print(i)

def spam11():
	supplies = ['pens','staplers','flamethrowers','binders']
	# for i in supplies:
	#  	print('index ' + str(supplies.index(i)) + ' in supplies is ' + i)
	for i in range(len(supplies)):
		print('Index ' + str(i) + ' in supplies is ' + supplies[i])

def spam12():
	spam = ['cat','dog','horse','rat','mouse']
	return 'cat' not in spam

def isNameInCat():
	catNames = []
	searchName = str(input('Please input the name you search for: '))
	print('Please input the names of the cats: ')
	while True:
		name = input()
		if name == '':
			break
		else:
			catNames.append(name)
	if searchName in catNames:
		print('You own a cat named ' + searchName)
	if searchName not in catNames:
		print('You dont own a cat named ' + searchName)

def spam13():
	cat = ['fat','gray','loud']
	size,color,disposition = cat
	print(size)

def spam14():
	spam = ['cat','dog','horse','rat','mouse']
	print(random.choice(spam))

import random
def spam15():
	spam = ['cat','dog','horse','rat','mouse']
	random.shuffle(spam)
	print(spam)

def spam16():
	spam = 5
	while spam < 50:
		spam *= 2
	print(spam)

def spam17():
	bacon = 'Zophie'
	bacon *= 3
	print(bacon)

def spam18():
	spam = ['cat','dog','horse','rat','mouse']
	spam.insert(1,'lol')
	print(spam)

def spam19():
	spam = ['cat','dog','horse','rat','mouse']
	spam.remove('dog')
	print(spam)
	del spam[-1]
	print(spam)

def spam20():
	spam = [3,1,2,5,6,1,2]
	spam.sort()
	print(spam)
	spam = ['cat','dog','horse','rat','mouse','Hound']
	spam.sort(key=str.lower)
	print(spam)
	# spam.reverse()
	# print(spam)

def magic8Ball():
	answer = ['yes','no','maybe']
	question = input('What is your question? \n')
	print(random.choice(answer))

def spam21():
	name = 'Zophie a cat'
	newName = name[0:7] + 'the ' + name[9:]
	print(name)
	print(newName)

def spam22():
	eggs = ('hello',42,0.5)
	print(eggs[1])
	print(eggs)
	print(type(eggs))
	eggs = list(eggs)
	print(type(eggs))
	print(list('Hello'))

def spam23():
	print(id('Howdy'))
	spam = [1,2,3]
	print(id(spam))
	print(id(spam[0]))

def spam24():
	hotdog = [1,2,3,4]
	cheese = hotdog
	print(hotdog, id(hotdog)),print(cheese, id(cheese))
	cheese[1] = 'Hello'
	print(hotdog, id(hotdog)),print(cheese, id(cheese))

def eggs(someParameter):
	someParameter.append('Hello')

def spam25():
	spam = ['A','B','C','D']
	cheese = copy.copy(spam)
	cheese[1] = 42
	print(spam)
	print(cheese)

import random, time, copy
def GameOfLife():
	WIDTH = 60
	HEIGHT = 20

	nextCells = []
	for x in range(WIDTH):
		column = []
		for y in range(HEIGHT):
			if random.randint(0,1) == 0:
				column.append('#')
			else:
				column.append(' ')
		nextCells.append(column)

	while True:
		print('\n\n\n\n\n')
		currentCells = copy.deepcopy(nextCells)

		for y in range(HEIGHT):
			for x in range(WIDTH):
				print(currentCells[x][y], end='')
			print()

		for x in range(WIDTH):
			for y in range(HEIGHT):
				leftCoord = (x - 1) % WIDTH
				rightCoord = (x + 1) % WIDTH
				aboveCoord = (y - 1) % HEIGHT
				belowCoord = (y + 1) % HEIGHT

				numNeighbors = 0
				if currentCells[leftCoord][aboveCoord] == '#':
					numNeighbors += 1 
				if currentCells[x][aboveCoord] == '#':
					numNeighbors +=1
				if currentCells[rightCoord][aboveCoord] == '#':
					numNeighbors += 1
				if currentCells[leftCoord][y] == '#':
					numNeighbors += 1
				if currentCells[rightCoord][y] == '#':
					numNeighbors += 1
				if currentCells[leftCoord][belowCoord] == '#':
					numNeighbors += 1
				if currentCells[x][belowCoord] == '#':
					numNeighbors += 1
				if currentCells[rightCoord][belowCoord] == '#':
					numNeighbors += 1

				if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
					nextCells[x][y] = '#'
				elif currentCells[x][y] == '' and numNeighbors == 3:
					nextCells[x][y] = '#'
				else:
					nextCells[x][y] = ' '
		time.sleep(1)

def CommaCode():
	spam = ['rat','horse','cat','dog','mouse']
	newSpam = []
	if len(spam) == 0:
		print('You wont get any food')
	else:
		for i in range(0,len(spam)-1):
			newSpam.append(spam[i] + ', ')
		newSpam.append(spam[-1])
		newSpam.insert(-1,'and ')
		print('You will be served ' + ''.join(newSpam))
CommaCode()

def CommaCode1():
	spam = ['rat','horse','cat','dog','mouse']
	if len(spam) == 0:
		print('You wont get any food')
	else:
		new = ', '.join(spam[:-1])
		new = new + ', and ' + spam[-1]
		print('You will be served ' + new)
CommaCode1()


import random
def CoinFlipStreaks():
	coinList = []
	while len(coinList) < 10000:
		if random.randint(0,1) == 0:
			coinList.append('H')
		else:
			coinList.append('T')
		coinCount = 0
		for i in range(len(coinList)-6):
			if (coinList[i] == 'H' and coinList[i+1] == 'H' and coinList[i+2] == 'H' and coinList[i+3] == 'H' and coinList[i+4] == 'H' and coinList[i+5] == 'H') or (coinList[i] == 'T' and coinList[i+1] == 'T' and coinList[i+2] == 'T' and coinList[i+3] == 'T' and coinList[i+4] == 'T' and coinList[i+5] == 'T'):
				coinCount += 1
	print(coinCount)










