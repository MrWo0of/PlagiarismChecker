from collections.abc import MutableMapping

# Mapper class created from MutableMapping base.
# MOSTLY FROM 'DATA STRUCTURES AND ALGORITHMS IN PYTHON' by Goodrich, et al.
class Mapper(MutableMapping):
    __slots__ = '_key', '_value', '_table'

    # Nested class used to store key-value pairs, do comparisons
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

        def __gt__(self, other):
            return self._key > other._key

        def __le__(self, other):
            return self._key <= other._key

        def __ge__(self, other):
            return self._key >= other._key

    # Map initialized with empty list for table
    def __init__(self):
        self._table = []

    # Get item by checking if key in table and returning item
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key not in dict')

    # Set item for key or change value of key if key exists
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._key = v
                return
        self._table.append(self.Item(k, v))

    # Search for item then remove key-value pair from table
    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(k)
                return
        raise KeyError('Key does not exist')

    # Give length of map
    def __len__(self):
        return len(self._table)

    # Allow for iteration over map
    def __iter__(self):
        for item in self._table:
            yield item._key

    # Comparison functions
    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


# Class created for file-splitting functions
class FileSplitter:

    #Separate function created to accept file from user
    def separate(self, file):
        # Map storing lines and line number created, file split by sentences
        lineMap = Mapper()
        lineNum = 1
        openedFile = open(file, 'r', encoding='mbcs')
        lines = openedFile.read().split('.')

        # For loop strips lines of newline characters, organizes words
        # in sentences alphabetically and reappends to map
        for line in lines:
            currentLine = line.strip('\n')
            sepLine = currentLine.split(' ')
            sepLine.sort()
            lineMap[lineNum] = sepLine
            lineNum += 1
        return lineMap

    # Function for comparing two maps created
    def compare(self, dict1, dict2):

        # Variable created.  Will be accumulated per exact match of words in
        # line then divided by length of smaller file to find total percent of same lines
        score = 0

        # Check if dict1 is larger than dict2, then use dict2 as base file for checks
        if len(dict1) >= len(dict2):
            size = len(dict2)
            for i in range(len(dict2)):
                if dict2[i + 1] in dict1.values() and dict2[i + 1] != '':
                    score += 1

        # Elif dict2 is larger, use dict1 for checks instead
        elif dict1 < dict2:
            size = len(dict1)
            for i in range(len(dict1)):
                size = len(dict1)
                if dict1[i + 1] in dict2.values() and dict1[i + 1] != '':
                    score += 1

        # Catch for empty files being used
        else:
            raise IndexError('One of the maps is empty')

        # Percent calculated then returned to user
        total = round(score / size, 2)
        return total
