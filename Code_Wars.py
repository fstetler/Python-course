# Code wars 

import string
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
