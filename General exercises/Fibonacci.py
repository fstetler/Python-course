"""Write a program that asks the user how many Fibonnaci numbers to generate and then 
generates them. Take this opportunity to think about how you can use functions. Make 
sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: 
The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
is the sum of the previous two numbers in the sequence. The sequence looks like 
this: 1, 1, 2, 3, 5, 8, 13, …)"""

def Fibonnaci():
	return int(input("How many fibonnaci numbers do you want"))

num = Fibonnaci()
if num == 1:
	b = [1]
elif num !=1:
	b = [1,1]
	for i in b:
		if len(b) < num:
			i = b[-1] + b[-2]
			b.append(i)
print(b)




