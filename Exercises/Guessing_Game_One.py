"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to 
guess the number, then tell them whether they guessed too low, too high, or exactly 
right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, 
print this out."""


import random
rand = random.randint(1,9)

guessing = True
count = 0

while guessing:
	
	print("This is the random number youre not supposed to see: " + str(rand))
	
	guess = input("Please guess on a number between zero and ten. Write 'exit' to exit and 'count' to see how many tries you had: ")

	
	
	if guess == "exit":
		break
	if guess == "count":
		print("Your count was " + str(count))
		break
	
	count += 1
	
	guess = int(guess)

	if guess < rand:
		print("You guessed too low")
	if guess > rand:
		print("You guessed too high")
	if guess == rand:
		print("You guessed exactly right, and it took only " + str(count) + " tries!")

		guessing = False







































"""import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess =! "exit":
	guess = input("What's youre guess?")

	if guess == "exit":
		break

	guess = int(guess)
	count += 1

	if guess < number:"""
		