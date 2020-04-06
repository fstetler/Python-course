# Organizing files

import shutil, os
from pathlib import Path
def spam1():
	p = Path('C:/Python-course/AutomateTheBoringStuff/Testingfiles')
	shutil.copy(p/'spam.txt',p/'some_folder')

spam1()