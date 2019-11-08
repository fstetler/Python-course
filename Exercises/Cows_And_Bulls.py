"""Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the 
user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed 
correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” 
and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the 
number of guesses the user makes throughout teh game and tell the user at the end."""



import random


rand = str(random.randint(1000,9999))

print(rand)

playing = True
while playing:

	cow = 0
	bull = 0
	
	guess = input("Please input a four digit number: \n")
	guess = str(guess)

	for i in range(0,4):
		if guess[i] == rand[i]:
			cow += 1
		elif rand[i] == guess:
					bull += 1


	print(cow)
	print(bull)
	if cow == 4:
		playing = False
		

print("Youve won")
	