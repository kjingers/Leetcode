'''
Smallest range: smallest difference between largest and smallest
element that contains a number from all lists.

- Can use K Way Merge to store one element from each array into Min Heap
- Can keep track of the largest value inserted into array
- Each loop, calculate max - min. Update global min if needed.

- If ranges are the same, the one with the smallest element is smaller
'''

from heapq import *
import math

def find_smallest_range(lists):
  minHeap = []
  resultMin = 0
  resultMax = math.inf
  currMax = -math.inf

  # If any list is empty, then no valid answer
  if any(list is False for list in lists):
    return [-1, -1]

  # minHeap contains (value, index, list)
  # Push the first element from each list onto minHeap
  for list in lists:
    if list is not None:
      heappush(minHeap, (list[0], 0, list))
      currMax = max(currMax, list[0])

  while len(minHeap) == len(lists):
    val, index, list = heappop(minHeap)
    
    # If current Max and Min is smaller than previous, then update
    if (currMax - val) < (resultMax - resultMin):
      resultMax = currMax
      resultMin = val

    # Push next element of list into minHeap
    # Update current Max value in heap
    if index + 1 < len(list):
      heappush(minHeap, (list[index + 1], index + 1, list))
      currMax = max(currMax, list[index + 1])

  return [resultMin, resultMax]



def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
  print("Smallest range is: " +
        str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))


main()

