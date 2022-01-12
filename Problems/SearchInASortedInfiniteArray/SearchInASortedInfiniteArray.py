'''
Before a normal binary search, we need to determine the start and end bounds. 
We do this by beginning with start = 0, end = 1, and keep doubling until key < arr[end]. 
Then we perform binary search on these bounds.
'''

import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
  
  # First, find range to search in
  # start with 2 and keep doubling size
  start, end = 0, 1
  while key > reader.get(end):
    newStart = end + 1
    end += (end - start + 1) * 2
    start = newStart

  return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):

  while start <= end:
    mid = start + (end - start) // 2
    if key < reader.get(mid):
      end = mid - 1
    elif key > reader.get(mid):
      start = mid + 1
    else: # reader.get(mid) == key
      return mid

  return -1


def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()







