'''
Similar to the original version. To allow for dupliates, instead of a dictionary of value->index, we can use a dictionary of value->set of indexes.
'''

from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.indexes = defaultdict(set)
        self.data = []
                

    def insert(self, val: int) -> bool:
        inSet = False
        if val not in self.indexes:
            inSet = True
            
        self.indexes[val].add(len(self.data))
        self.data.append(val)
        return inSet
        
    def remove(self, val: int) -> bool:
        if val in self.indexes:
            idx = self.indexes[val].pop()
            last = self.data[-1]
            self.data[idx] = last
            self.indexes[last].add(idx)
            self.indexes[last].remove(len(self.data) - 1)
            self.data.pop()
            if len(self.indexes[val]) == 0:
                del self.indexes[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
