import glob
import os

os.chdir('../Blockchain/Test')

for i in glob.glob('*.py'):
    print(i)