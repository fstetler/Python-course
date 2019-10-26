"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords 
have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, 
generating a new password every time the user asks for a new password. 

Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word"""

import string

def random(x):
	
	# Define lists of capital letters, lower case letters, and numbers

	smalletter = list(string.ascii_lowercase)
	bigletter = list(string.ascii_uppercase)
	number = list(range(0,10))

	password = []

	start = 0

	# For the length of the password, randomize either a capital, lower, or number in each item

	while start <= x-1:

		import random

		a = random.choice([smalletter, bigletter, number])
		b = random.choice(a)
	
		password.append(b)
		start += 1
		
	return password


# Continue to run while generating is True

Generating = True

while Generating:

	word = str(input("Let's create a password. Do you want to create one yourself (press 1) or generate one (press 2)?: \n"))

	# If 1, wrote your own word as a password

	if word == "1":
		pw_self = str(input("Write what you want your password to be: \n"))
		print("Your password is " + pw_self)
		Generating = False

	# If 2, decide the length of your password
	
	elif word == "2":
		
		length = int(input("How long do you want the password to be? \n"))
		password = random(length)
		pw = [str(i) for i in password]
		pw_joined = "".join(pw)

		print("Your password is now " + pw_joined)

		Generating = False

	# If neither 1 or 2, repeat the process

	else:
		print("That is not an option. \n")


