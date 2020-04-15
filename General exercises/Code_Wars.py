# Code wars 

import string
def consonant():
	s = 'khrushchev'
	s = list(s)
	value = {}
	letters = string.ascii_lowercase
	for i in range(len(letters)):
		value[letters[i]] = i+1 
	print(s)
	vowels = ['a','o','u','i','e']
	consonant = []

	for i in s:
		if i in vowels:
			s[s.index(i)] = ' '
	newS = (''.join(s)).split(' ')
	print(newS)
	maxValue = []
	for i in newS:
		sumValue = 0
		for j in i:
			sumValue += value[j]
		maxValue.append(sumValue)
	print(max(maxValue))		

def teenText(phrase):
	phrase = phrase.lower()
	letters = list(string.ascii_lowercase)
	numbers = list(string.digits)
	all = letters + numbers
	a = [1,2,3]
	b = [1,2,3,4]
	c = [1]
	d = [4]
	e = [5]
	space = [1,2]
	pointsLetters = a*5 + b + a + b
	pointsNumbers =  [space[1]] + c + d*5 + e + d + e
	points = pointsLetters + pointsNumbers
	value = {}
	for i in range(len(all)):
		value[all[i]] = points[i] 
		value[' '] = space[1]
		value['#'] = 1
		value['*'] = 1
	sum = 0
	for j in phrase:
		sum += value[j]	
	#print(value)
	print(sum)

# BUTTONS = [ '1',   'abc2',  'def3',
#           'ghi4',  'jkl5',  'mno6',
#           'pqrs7', 'tuv8', 'wxyz9',
#             '*',   ' 0',    '#'   ]

def presses(phrase):
	sum = 3
	for button in BUTTONS:
		
		for c in phrase.lower():
			
			if c in button:
				a = button.find(c)
				sum += a
	print(sum)

def find_it(seq):
	
	for i in seq:
		if seq.count(i) != 2:
			return i
	
def max_ball(v0):
	# Max height is height derivative and where h' is zero
	# h = v*t - 0.5*g*t*t
	# g = 9.81
	#h_prim = v - 0.5*g*t*2 => t = v/(g) if h_prim = 0

	g = 9.81
	v0 = v0/3.6
	t = v0/g
	print(round(t*10))

def stat(strg):
	sec = []
	for i in range(len(strg)):
		time = strg.split(', ')
	
	for j in time:
		timeSec = j.split('|')
		sec.append(timeSec)
	for k in sec:
		#print(k)
		if k[0][0] == '0':
			k[0] = k[0][1]
	
	timeSec = []
	for l in sec:#range(len(sec)-1):
		seconds = int(l[0])*3600 + int(l[1])*60 + int(l[2])
		timeSec.append(seconds)
	
	# Turn the time difference into range between them in hours, minutes, and seconds
	timeDif = max(timeSec) - min(timeSec)
	rangeHour = timeDif // 3600
	rangeMin = (timeDif - rangeHour*3600) // 60
	rangeSec = (timeDif - rangeHour*3600 - rangeMin*60)
	rangeTot = [rangeHour, rangeMin, rangeSec]
	
	print(rangeTot)

	# Turn the time difference into average
	totAve = 0
	for m in timeSec:
		totAve += m
	averageTot = totAve/len(timeSec)
	rangeHourAve = averageTot // 3600
	rangeMinAve = (averageTot - rangeHourAve*3600) // 60
	rangeSecAve = (averageTot - rangeHourAve*3600 - rangeMinAve*60)
	AveTot = [int(rangeHourAve), int(rangeMinAve), round(rangeSecAve)]
	print(AveTot)

#strg = ("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")
#stat(strg)

def likes(names):
	if len(names) == 0:
		return 'no one likes this'
	elif len(names) == 1:
		return names[0] + ' likes this'
	elif len(names) == 2:
		return names[0] + ' and ' + names[1] + ' likes this'
	elif len(names) == 3:
		return names[0] + ', ' + names[1] + ' and ' + names[2] + ' likes this'
	elif len(names) > 3:
		return names[0] + ', ' + names[1] + ' and ' + str((len(names) - 2)) + ' likes this' 

#print(likes(names = ['Alex', 'Jacob', 'Mark', 'Max']))

def highest_rank(arr):
	maxCount = []
	maxList = []
	for i in arr:
		maxCount.append(arr.count(i))
	for j in arr:
		if arr.count(j) == max(maxCount):
			maxList.append(j)
	maxList.sort()
	return maxList[-1]

# arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10, 10]
# print(highest_rank(arr))

def duplicate_count(text):
	# IMPOSSIBLE
	c = 0
	text = list(text)
	for i in text:
		#print(text.index(i))
		if i in text[text.index(i)+1:]:
			c += 1
			text = list(filter(lambda a: a != i , text))

	print(c)
			



#def iter_pi(epsilon):

#A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
def job1(A):
	singleList = []
	
	for i in A:
		if i > -10 and i < 10:
			singleList.append(i)
	if len(singleList) > 0:
		return max(singleList)
	else:
		return 'No value'


#print(job1(array))
T = [3,4,7,7,6,6]
def job2(T):
	len_T = len(T)
	while len(T) > len_T/2:
		c = []	
		for i in T:
			c.append(T.count(i))
		del T[c.index(max(c))]
	return T
#print(job2(T))
	
def job3(N):
	numbers = [0,1,1]
	while len(numbers) < 100000:
		while len(str(numbers[-1])) < 2:
			if len(str(numbers[-2])) > 1:
				add = numbers[-1] + int(str(numbers[-2])[0]) + int(str(numbers[-2])[1])
				numbers.append(add)
			else:
				add = numbers[-1] + numbers[-2]
				numbers.append(add)

		while len(str(numbers[-1])) > 1:
			if len(str(numbers[-2])) > 1:
				add = int(str(numbers[-1])[0]) + int(str(numbers[-1])[1]) + int(str(numbers[-2])[0]) + int(str(numbers[-2])[1])
				numbers.append(add)
			else:
				add = int(str(numbers[-1])[0]) + int(str(numbers[-1])[1]) + int(numbers[-2])
				numbers.append(add)
	

	return numbers[N]

def iter_pi(epsilon):
	#i_list = []
	#c = 2
	# for i in range(100):
	# 	if c % 2 == 0:
	# 		i_list.append(1)
	# 	else:
	# 		i_list.append(-1)
	# 	c += 1

	# newList = []
	# for j in range(0,100,2):
	# 	newList.append(j)
	# #print(newList)

	# f_list = []
	# for i in newList:
	# 	f_list.append(i*i_list[newList.index(i)])
	# print(f_list)
	

	pi = 4
	pi_real = 3.14159265
	n = 1
	i = -1
	print(pi-pi_real)
	while abs(pi - pi_real) > epsilon:
		pi = pi + 4*i/((1 + 2*n))
		print(pi)
		n += 1
		print(n)
		i *= -1
		print(i)
		print(pi)
			
def disemvowel(string):
	#print(string)
	#string = string.split()
	string = list(string)
	#print(string)
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	newString = []
	for i in string:
		print(i)
		for letter in i:
			print(letter)
			if letter not in vowels:
				newString.append(letter)
	print(newString)			
	#print(newString)
	#print(string)
	#print(vowels)
	print(''.join(newString))

def solution(number):
	natNumb = []
	for i in range(1,number):
		if i % 3 == 0 or i % 5 == 0:
			natNumb.append(i)
	return sum(natNumb)

def openOrSenior(data):
	OpenOrSeniorList = []
	for i in data:
		if i[0] >= 55 and i[1] > 7:
			OpenOrSeniorList.append('Senior')
		else:
			OpenOrSeniorList.append('Open')
	return OpenOrSeniorList


def xo(s):
	xlist = list(s)
	countx = 0
	counto = 0
	for i in xlist:
		if i.lower() == 'o':
			counto += 1
		elif i.lower() == 'x':
			countx += 1
	if countx == counto:
		return True
	else:
		return False

def accum(s):
	c = 0
	newString = []
	for i in s:
		newString.append(i.upper() + i.lower()*c + '-')
		c += 1	
	string = ''.join(newString)
	print(string[:-1])

def tower_builder(n_floors):
	tower = []
	c = 1
	for i in range(n_floors,0,-1):
		length = len(range(n_floors))
		tower.append(' '*(i-1) + '*'*c + ' '*(i-1))
		c += 2
	print(tower)

def calculator():
	def zero(x):
		if x == '+':
			return 
		return 0
	def one():
		return 1
	def two():
		return 2
	def plus():
		return '+'

	print(zero())

def is_isogram(string):
	if string == '':
		return True
	else:
		#print(string)
		string = list(string.lower())
		#print(string)
		#print(string[:string.index('v')] + string[string.index('v')+1:])
		for i in string:
			if i in string[:string.index(i)] + string[string.index(i)+1:]:
				return False
			else:
				return True

def is_isogram2(string):
	if string == '':
		return True
	else:
		countList = []
		string = list(string.lower())
		print(string)
		print(string.count('o'))
		for i in string:
			countList.append(string.count(i))
		print(countList)
		for j in countList:
			if j > 1:
				return False
			else:
				return True
		print(countList)

def check_coupon(entered_code, correct_code, current_date, expiration_date):

	def MonthToNumber(Month):
		MonthNum = {
					'January': 1,
					'February': 2,
					'March': 3,
					'April': 4,
					'May': 5,
					'June': 6,
					'July': 7,
					'August': 8,
					'September': 9,
					'October': 10,
					'November': 11,
					'December': 12
					}

		return MonthNum[Month]

	month_current_num = MonthToNumber(current_date.split()[0])
	month_expiration_num = MonthToNumber(expiration_date.split()[0])

	if entered_code != correct_code:
		return False
	else:
		if current_date.split()[-1] > expiration_date.split()[-1]:
			if month_current_num > month_expiration_num:
				if current_date.split()[-2][:-1] > expiration_date.split()[-2][:-1]:
					return False
		else:
			return True
	

def gimme(input_array):
	#sortedList = input_array.sorted
	print(sorted(input_array)[1])

def sum_digits(number):
	numListStr = list(str(number))
	sumNum = 0
	if numListStr[0] == '-':
		for i in numListStr[1:]:
			sumNum += int(i)
		return sumNum
	else:
		for i in numListStr:
			sumNum += int(i)
		return sumNum


def high_and_low(numbers):
	numList = numbers.split()
	numListSort = sorted(numList, key = int)
	print(numList)
	print(numListSort)

def row_sum_odd_numbers(n):
	rowList = []
	if n == 1:
		return 1
	# 1 3 6 10 15
	step = 1 + (2*(n-1))
	for i in range(1,1 + (2+2*n)):
		print(i)
	#digits = 1 + (2*(n-1))    
	# for i in range(1,n+n*):
	# 	digits = 1 + (2*(i-1))
	# 	rowList.append(digits)
	#print(rowList)

def find(n):
	c = 0
	for i in range(n+1):
		print(i)


def to_jaden_case(string):
	stringList = string.split()
	print(stringList)
	newSentence = []
	for i in stringList:
		newSentence.append(i.capitalize())
	print(''.join(newSentence))


def divisors(n):
	c = 0
	for i in range(1,int(n/2)+1):
		if i % 2 == 0:
			c += 1
		elif i % 3 == 0:
			c += 1
		elif i % 5 == 0:
			c += 1
	print(c) 

n = 5
divisors(n)













