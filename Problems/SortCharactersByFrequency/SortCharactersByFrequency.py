from heapq import *
from collections import Counter

def sort_character_by_frequency(str):

  maxHeap = []
  result = []

  # Create a hash map of char -> count
  counts = Counter(str)

  # Add all distinct characters and counts to maxHeap
  for char, count in counts.items():
    heappush(maxHeap, (-count, char))

  # Pop one distinct character at a time from maxHeap
  while maxHeap:
    count, char = heappop(maxHeap)
    # Add character "count" times to result string
    for i in range(-count):
      result.append(char)


  return ''.join(result)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
