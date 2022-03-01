'''
There are a few data structures that can insert and delete in O(1 time) (like set). However,
we need something that can get random in O(1) time. A set does not support random choice.

We can use a list to get random by generating a random number between 0 and len(arr) - 1, and using that as index.

Of course, we can append to list in O(1) time. But removing from list requires O(n) to shift all elemtns. To get around this, we can use a dict to map the value to index in the list. When we want to remove a value, we switch the value with the last element in the list. Then, we pop it from the end of the list. We update the dict accordingly


'''

import random

class RandomizedSet:

    def __init__(self):
        self.indexes = {}
        self.values = []
        

    def insert(self, val: int) -> bool:
        if val not in self.indexes:
            self.indexes[val] = len(self.values)
            self.values.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.indexes:
            idx = self.indexes[val]
            lastVal = self.values[-1]
            self.values[idx] = lastVal
            self.indexes[lastVal] = idx
            self.values.pop()
            del self.indexes[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
