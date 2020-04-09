# Highest single digit value
def job1(A):
	singleList = []
	for i in A:
		if i > -10 and i < 10:		# Only values between -10 and 10, i.e singel digit values
			singleList.append(i)	# Adds those values to a list
	if len(singleList) > 0:			
		return max(singleList)		# Takes the max value in that list, assuming it has values
	else:
		return 'No value'

# Marys candies
def job2(T):
	len_T = len(T)
	while len(T) > len_T/2:			# Remove a candy as long as there are more than half left
		c = []	
		for i in T:
			c.append(T.count(i))	# Count how many of each candy there are
		del T[c.index(max(c))]		# Remove one candy of which there are most of
	return T						# Return the new list T
	
# Two values before added
def job3(N):
	numbers = [0,1,1]
	while len(numbers) < 10000000:	
		while len(str(numbers[-1])) < 2:			# while the last number is singel digit
			if len(str(numbers[-2])) > 1:			# if the next to last number is double digit
				add = numbers[-1] + int(str(numbers[-2])[0]) + int(str(numbers[-2])[1])			# Create a number which adds the last number plus the two digits from the second to last
				numbers.append(add)					# Add that number to the list
			else:
				add = numbers[-1] + numbers[-2]		# if the next to last number is singel digit add the last and second to last value
				numbers.append(add)					# Add that number to the list

		while len(str(numbers[-1])) > 1:			# while the last number is double digit
			if len(str(numbers[-2])) > 1:			# if the next to last number is double digit
				add = int(str(numbers[-1])[0]) + int(str(numbers[-1])[1]) + int(str(numbers[-2])[0]) + int(str(numbers[-2])[1])	# Create a number which adds the two values from the last number and the two values from the next to last number
				numbers.append(add)					# Add that number to the list
			else:
				add = int(str(numbers[-1])[0]) + int(str(numbers[-1])[1]) + int(numbers[-2])	# if the next to last number is singel digit add the two values from the last value and the second last value
				numbers.append(add)					# Add that number to the list
	
	return numbers[N]								# Return the Nth value of numbers