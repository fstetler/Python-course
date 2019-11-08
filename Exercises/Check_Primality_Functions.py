"""Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this 
opportunity to practice using functions, described below."""

def number():
	return int(input("Give me a number: \n"))

check = number()
b = list(range(0,check+1))
print("Check = " + str(check))
print("b = " + str(b[1:]))


#print(isinstance(check,int))
#print(b[1:check])
#print(isinstance(b[-1],str))


#a = []
#for i in b:
#	a.append(str(i))

#print(a[1:check])

for i in b[1:]:
	if check % i  == 0:
		print('This is not a prime')
	else:
		print('This is a prime')







