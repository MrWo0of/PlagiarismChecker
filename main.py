import os
from difflib import SequenceMatcher

# Directory variable.
direc = 'Files/'
fileList = [direc + f for f in os.listdir(direc) if f.endswith('.txt')]
checkFile = input('Enter the file\'s path to check for plagiarism: ')
checkFileName = checkFile.strip('.txt')
checkFile = open(checkFile, 'r')
checkFileRead = checkFile.read()


documents = [open(f).read() for f in fileList]


for filename, document in zip(fileList, documents):
    ab = SequenceMatcher(None, document, checkFileRead).ratio()
    result = int(ab * 100)
    if result >= 50:
        print(f'Potential plagiarism detected in {checkFileName} matching {result}% with {filename}')

