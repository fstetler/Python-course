# Organizing files

import shutil, os
from pathlib import Path
p = Path('C:\Python-course\AutomateTheBoringStuff')
shutil.copy(p/'spam.txt',p/'some_folder')
