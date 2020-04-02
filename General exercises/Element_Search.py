"""Write a function that takes an ordered list of numbers (a list where the elements 
are in order from smallest to largest) and another number. The function decides whether 
or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search."""

import random


def find(a, rand):

	for i in a:
		if i == rand:
			return True
	return False

rand = random.randint(0,9)
a = list(range(0,10,2))

print(find(a,rand))




