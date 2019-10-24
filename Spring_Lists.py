"""Ask the user for a string and print out whether this string is a 
palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)"""

palindrome = str(input("Please type a word: "))

back = palindrome[::-1]
#back = word[::1]

if back == palindrome:
	print("This is a palindrome")
else:
	print("This is not a palindrome")