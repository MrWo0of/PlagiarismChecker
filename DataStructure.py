from collections import MutableMapping
class HomebrewMap(MutableMapping):
    __slots__ = '_key', '_value'

    class Item:


class FileSplitter:
    def __init__(self):
        percent = 0


    def separate(self, file):
        lineDict = {}
        lineNum = 1
        openedFile = open(file, 'r', encoding='mbcs')
        for line in openedFile:
            currentLine = line.strip('\n')
            sepLine = currentLine.split(' ')
            sepLine.sort()
            lineDict[lineNum] = sepLine
            lineNum += 1
        return lineDict

    def compare(self, dict1, dict2):
        pass