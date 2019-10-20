"""Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this 
opportunity to practice using functions, described below."""

def number():
	return int(input("Give me a number"))

check = number()
b = list(range(0,number+1))

for i in b:
	if check % i == 0:
		print
	