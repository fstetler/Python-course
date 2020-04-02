# Pattern matching with regular expressions

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	else:
		return True

def checkPhoneNumber():

	message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

	for i in range(len(message)):
		if isPhoneNumber(message[i:i+12]):
			print(message[i:i+12] + ' is a phone number')

import re
def isPhoneNumber2():
	phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
	mo = phoneNumRegex.search('My number is 415-555-4242.')
	print('Phone number found: ' + mo.group())
	areaCode, mainNumber = [mo.group(1),mo.group(2)]
	print('Area code is ' + areaCode)
	print('Main number is ' + mainNumber)

def testRe():
	number = re.compile(r'\d{4} \d{2} \d{3} \d{2}')
	hey = number.search('This is a bank number 3413 43 341 31')
	print('Bank number found: ' + hey.group())

def hero1():
	heroRegex = re.compile(r'Batman|Tina Fey')
	mo1 = heroRegex.search('Batman and Tina Fey')
	print(mo1.group())

def hero2():
	batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
	mo = batRegex.search('Its a cool Batcopter and a cool Batmobile')
	print(mo.group())

def hero3():
	batRegex = re.compile(r'Bat(wo)?man')
	mo1 = batRegex.search('The adventures of Batman')
	print(mo1.group())

def reTest():
	text = 'Two people mentioned are Oski, and John'
	search = re.compile(r'Oski|John|Albin|Petter')
	mo = search.search(text)
	print(mo.group())

def reFindAll():
	text = 'Two people mentioned are Oski, and John'
	search = re.compile(r'Oski|John|Albin|Petter')
	mo = search.findall(text)
	print(mo[0])
	print(mo[1])

def FindAllRe():
	text = 'Phone: 513-535-6444, Work: 513-753-3555'
	phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
	mo = phoneRegex.findall(text)
	print('Phone: ' + mo[0] + ', work: ' + mo[1])

def vowel():
	vowelRegex = re.compile(r'a|e|i|o|u|y|A|E|I|O|U|Y')
	mo = vowelRegex.findall('This is a sentence HELLO')
	print(mo)

def testSearchWord():
	wordRegex = re.compile(r'bitch|sal(mon|sitcha)')
	mo = wordRegex.findall('This thing contains salsitcha, bitch')
	print(mo)

def at():
	atRegex = re.compile(r'..at')
	mo = atRegex.findall('The cat in the hat shat on the mat that')
	print(mo)

# import re
# sentence = "is2 Thi1s T4est 3a"
# splitSentence = sentence.split()
# newSentence = ('a '*len(splitSentence)).split()
# for i in splitSentence:
# 	print(i)
# 	regex = re.compile(r'\d')
# 	mo = regex.search(i)
# 	print(mo.group())
# 	print(int(mo.group())-1)
# 	newSentence[int(mo.group())-1] = i
# print(newSentence)
# print(' '.join(newSentence))














