from heapq import *
from collections import Counter

def find_maximum_distinct_elements(nums, k):

      distinctCount = 0
      minHeap = []

      # Create a hashmap of characters with counts
      counts = Counter(nums)

      # Put all non-distinct characters with count > 1
      # into a minHeap by count. Increment distinctCount for each
      # distinct character
      for num, count in counts.items():
            if count > 1:
                  heappush(minHeap, count)
            else: # count == 1
                  distinctCount += 1

      # Pop from minHeap. Make each character distinct until
      # no more non-distinct characters, or k <= 0
      while minHeap and k > 0:
            count = heappop(minHeap)

            # Try to make distinct. Update k
            k -= (count - 1)

            # If k isn't negative, then we are successful in making
            # this char distinct
            if k >= 0:
                  distinctCount += 1


      # If no more non-distinct characters but k > 0, then must
      # remove k disctint characters

      if k > 0:
            distinctCount -= k

      return distinctCount



def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()

