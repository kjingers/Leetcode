'''
Everytime we need to push, we need to keep track of the number, frequency count, and sequence number
- sequence number allows the max heap to break frequency ties with sequence numer (more recent num)
- Can keep track of frequency count in a hash map
'''

from heapq import *

class Element:
  
  def __init__(self, number, frequency, sequenceNumber):
    self.number = number
    self.frequency = frequency
    self.sequenceNumber = sequenceNumber

  def __lt__(self, other):
    if self.frequency != other.frequency:
      return self.frequency > other.frequency
    return self.sequenceNumber > other.sequenceNumber

class FrequencyStack:

  maxHeap = []
  sequenceNumber = 0
  frequencyMap = {}

  def push(self, num):

    if num not in self.frequencyMap:
      self.frequencyMap[num] = 0

    self.frequencyMap[num] += 1

    heappush(self.maxHeap, Element(num, self.frequencyMap[num], self.sequenceNumber))

    self.sequenceNumber += 1

  def pop(self):
    element = heappop(self.maxHeap)
    self.frequencyMap[element.number] -= 1

    if self.frequencyMap[element.number] < 1:
      del self.frequencyMap[element.number]

    return element.number
    


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()







