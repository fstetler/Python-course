"""Write a program (function!) that takes a list and returns a new list that contains all the elements 
of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""

def listprogram(x):
	y = []
	for i in x:
		if i not in y:
			y.append(i)
	return y


a = [1,2,3,4,3,2,1]
print(listprogram(a))	