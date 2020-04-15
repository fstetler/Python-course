# Chapter 2

import random
def GuessTheNumber():
	
	randNum = random.randint(1,20)

	guess = int(input('I am thinking of a number between 1 and 20.\nTake a guess. \n'))
	print(randNum)
	guessing = True	
	while guessing:
		
		if guess > 20 or guess < 1:
			print('That number is outside of the guessing range')
		else:
			if guess < randNum:
				print('That number is too low, guess again.')
			elif guess > randNum:
				print('That number is too high, guess again.')
			elif guess == randNum:
				print('You guessed correct, the number is ' + str(guess))
				again = input('Want to play again? y or n: ')
				if again == 'y':
					guess = int(input('I am thinking of a number between 1 and 20.\nTake a guess. \n')) 
					randNum = random.randint(1,20)	
					print(randNum)				
					continue
				elif again == 'n':
					break
		guess = int(input())
