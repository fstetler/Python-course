"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords 
have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, 
generating a new password every time the user asks for a new password. Include your run-time code in a 
main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

def random(x):
	
	smalletter = list(string.ascii_lowercase)
	bigletter = list(string.ascii_uppercase)
	number = list(range(0,10))

	passwordlength = list(range(0,x))
	password = []

	start = 0

	while start <= x-1:

		import random

		a = random.choice([smalletter, bigletter, number])
		b = random.choice(a)
	
		password.append(b)
		start += 1
	return password



import string

Generating = True
while Generating:

	word = str(input("Lets create a password. Do you want to create one yourself (press 1), or generate one (press 2)?: \n"))

	if word == "1":
		pw_self = str(input("Write what you want your password to be: \n"))
		print("Your password is " + pw_self)
		Generating = False

	elif word == "2":
		
		length = int(input("How long do you want the password to be? \n"))

		password = random(length)

		pw = [str(i) for i in password]

		pw_joined = "".join(pw)

		print("Your password is now " + pw_joined)

		Generating = False

























"""import string

Generating = True
while Generating:

	word = str(input("Lets create a password. Do you want to create one yourself (press 1), or generate one (press 2)?: \n"))

	if word == "1":
		pw_self = str(input("Write what you want your password to be: \n"))
		print("Congratulations fuckface, your password is " + pw_self)
		break

	if word == "2":

		length = int(input("How long do you want the password to be? \n"))
		smalletter = list(string.ascii_lowercase)
		bigletter = list(string.ascii_uppercase)
		number = list(range(0,10))

		passwordlength = list(range(0,length))
		password = []


		start = 0

		while start <= length-1:

			import random

			a = random.choice([smalletter, bigletter, number])
			b = random.choice(a)
			
			password.append(b)
			start += 1

		pw = [str(i) for i in password]

		pw_joined = "".join(pw)

		print("Alright dumbass, your password is now " + pw_joined)

		break"""

