from difflib import SequenceMatcher
import Files


testFile = open('Files/Test1', 'r')
testFile2 = open('Files/Test2', 'r')

file1 = testFile.read()
file2 = testFile.read()

ab = SequenceMatcher(None, file1, file2).ratio()

print(int(ab * 100))