# Reading and writing files

from pathlib import Path

def spam1():
	myFiles = ['accounts.txt','details.csv','invite.docx']
	for filename in myFiles:
		print(Path(r'C:\Users\Al',filename))
spam1()