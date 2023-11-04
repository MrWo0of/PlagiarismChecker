import os
from difflib import SequenceMatcher

file = [f for f in os.listdir() if f.endswith('.txt')]
print(file)
'''
testFile = open('Files/Test1.txt', 'r')
testFile2 = open('Files/Test2.txt', 'r')

file1 = testFile.read()
file2 = testFile2.read()
print(file1, '\n', file2)

ab = SequenceMatcher(None, file2, file1).ratio()

result = int(ab * 100)
print(f'{result}% plagiarized')
'''