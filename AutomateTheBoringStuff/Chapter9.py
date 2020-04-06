# Reading and writing files

from pathlib import Path
import os

def spam1():
	myFiles = ['accounts.txt','details.csv','invite.docx']
	for filename in myFiles:
		print(Path(r'C:\Users\Al',filename))

def spam2():
	homeFolder = r'C:\User\Al'
	subFolder = 'spam'
	print(homeFolder + '\\' + subFolder)
	print('\\'.join([homeFolder,subFolder]))

def spam3():
	homeFolder = Path('C:/User/Al')
	subFolder = Path('spam')
	print(homeFolder / subFolder)

def spam4():
	os.makedirs('C:\\Python-course\\AutomateTheBoringStuff\\makedirsTest2')
	Path(r'C:\\Python-course\\AutomateTheBoringStuff\\NewmakdirsTest').mkdir()
	Path(r'C:\\Python-course\\AutomateTheBoringStuff\\NewmakdirsTest').rmdir()

def spam5():
	#return Path.cwd()
	return Path.cwd().is_absolute()

def spam6():
	p = Path('C:/Python-course/AutomateTheBoringStuff/Chapter10.py')
	print(p.name)

def spam7():
	print(Path.cwd())
	print(Path.cwd().parents[0])
	print(Path.cwd().parents[1])

def spam8():
	calcFilePath = 'C:\\Windows\\System32\\calc.exe'
	print(os.path.basename(calcFilePath))

def spam9():
	p = Path('C:/Python-course/AutomateTheBoringStuff/Chapter10.py')
	print(os.path.getsize(p))

def spam10():
	totalSize = 0
	for filename in os.listdir('C:/Python-course/AutomateTheBoringStuff/'):
		totalSize += os.path.getsize('C:/Python-course/AutomateTheBoringStuff/')

def spam11():
	p = Path('C:/Python-course/AutomateTheBoringStuff/')
	for textFilePathObj in p.glob('*.py'):
		print(textFilePathObj)

def spam12():
	fileExists = Path('C:/Python-course/AutomateTheBoringStuff/Chapter10.py')
	NotExistDir = Path('C:/Python-course/doesntexist')
	print(NotExistDir.is_dir())

from pathlib import Path
def spam13():
	p = Path('spam.txt') # Creates the path for the text file
	p.write_text('This contains new information') # Strings what the text file should contain
	hello = open('C:/Python-course/AutomateTheBoringStuff/spam.txt') # Creates what text file should be opened
	test = hello.read() # Reads the information in the file into test
	print(test) # prints the information

def spam14():
	# Create the file Bacon.txt with Bacon in int
	p = Path('Bacon.txt')
	p.write_text('Bacon')

	# Opens the Bacon.txt in write mode and adds Hello, World!
	baconFile = open('Bacon.txt','w')
	baconFile.write('Hello, world!\n')

	# Closes the file from write mode, opens it in append mode, and adds new text under
	baconFile.close()
	baconFile = open('bacon.txt','a')
	baconFile.write('New text under hello, world')

	# Closes file again, opens it regularly, reads the content into "content", closes file, and prints content
	baconFile.close()
	baconFile = open('bacon.txt')
	content = baconFile.read()
	baconFile.close()
	print(content)














