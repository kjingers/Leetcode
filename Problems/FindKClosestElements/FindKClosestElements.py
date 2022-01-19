'''
One option to solve (below) is to use binary search to find the closest value to X. 
Then add all diffs of nums from idx-K to idx+K to minHeap. 
Then, pop K numbers to get the K nums with the smallest difference.

Another option is to again use binary search to get closest value. 
But then use two pointers to comparedifferences on each side, and iterating accordingly. 
This has better time complexity.

A third option (on LC) is to just use binary search to find the left-most number of the answer. 
Then we return the subarray from arr[left:left+K]
'''

from heapq import *

def find_closest_elements(arr, K, X):
      result = []
      minHeap = []

      # Binary Search to find index of X. If X not present,
      # return index to left (unless at index 0)
      idx = binary_search(arr, X)

      # Make upperbound = index + K and lowerbound = index - K
      # Check for arr bound limits
      upperBound = min(len(arr) - 1, idx + K)
      lowerBound = max(0, idx - K)

      # Add all diffs from index - K to index + K to minHeap, where
      # diff = abs(num - X)
      for i in range(lowerBound, upperBound + 1):
            diff = abs(arr[i] - X)
            heappush(minHeap, (diff, arr[i]))

      # Pop K elements from minHeap to get K closest numbers
      for _ in range(K):
            diff, num = heappop(minHeap)
            result.append(num)

      # Return the result in sorted order
      return sorted(result)

def binary_search(arr, key):
      start, end = 0, len(arr) - 1

      while start <= end:
            mid = start + (end - start) // 2

            if key < arr[mid]:
                  end = mid - 1
            elif key > arr[mid]:
                  start = mid + 1
            else:
                  return mid

      # If not found, return index to the left
      return end


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
