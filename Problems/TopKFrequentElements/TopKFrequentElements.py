from collections import Counter
from heapq import *

def find_k_frequent_numbers(nums, k):
  minHeap = []
  result = []

  # Create Dict that maps nums to counts
  freqs = Counter(nums)

  for num, count in freqs.items():
    heappush(minHeap, (count, num))
    if len(minHeap) > k:
      heappop(minHeap)
  
  while minHeap:
    result.append(heappop(minHeap)[1])

  return result


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

