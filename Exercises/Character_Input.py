# Exercise 1
# Create a program that asks the user to enter their name and their age. Print out
# a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Please enter your name: ")
age = int(input("How old are you: "))
year = str((2019-age) + 100)
print(name + ", you will turn 100 the year " + year)
#print(name + ", you will turn 100")
#print(name, year)