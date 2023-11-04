from collections.abc import MutableMapping


class HomebrewMap(MutableMapping):
    __slots__ = '_key', '_value', '_table'

    class Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not self._key == other._key

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key not in dict')

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._key = v
                return
        self._table.append(self.Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(k)
                return
        raise KeyError('Key does not exist')

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key


class FileSplitter:
    def __init__(self):
        percent = 0


    def separate(self, file):
        lineMap = HomebrewMap()
        lineNum = 1
        openedFile = open(file, 'r', encoding='mbcs')
        for line in openedFile:
            currentLine = line.strip('\n')
            sepLine = currentLine.split(' ')
            sepLine.sort()
            lineMap[lineNum] = sepLine
            lineNum += 1
        return lineMap

    def compare(self, dict1, dict2):
        score = 0
        if len(dict1) >= len(dict2):
            size = len(dict2)
            for i in range(len(dict2)):
                print(i)
                if dict2[i + 1] in dict1.values():
                    score += 1
        elif dict1 < dict2:
            for i in range(len(dict2)):
                size = len(dict1)
                if dict1[i] in dict2.values():
                    score += 1
        total = round(size / score, 2)
        return total

filesplitter = FileSplitter()
dict1 = filesplitter.separate('sample-2.txt')
dict2 = filesplitter.separate('sample-3.txt')
print(filesplitter.compare(dict1, dict2))
