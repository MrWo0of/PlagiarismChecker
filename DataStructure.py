from collections.abc import MutableMapping
class HomebrewMap(MutableMapping):
    __slots__ = '_key', '_value'

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
        pass

map = HomebrewMap()


map.__setitem__('k', 'v')

print(map)