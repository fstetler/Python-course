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
	c = []
	number = 0
	for i in text:
		if i in text and not text[text.index(i)]:
			print('a')	
	# 	c.append(text.count(i))
	# print(c)
	# for j in c:
	# 	if j > 1:
	# 		number += j
	# print(int(number/4))

text = 'abcdea'
duplicate_count(text)

