from heapq import *

def find_sum_of_elements(nums, k1, k2):

  # We can use a Max Heap to keep track of the smallest K2 numbers
  # Then, once we've gone through the array, we can:
  # - Pop once
  # - Then add the next K2 - K1 - 1 Numbers from the top

  maxHeap = []

  # Loop through and add K2 elements to maxHeap
  # If maxHeap has more than K2 elements, the pop largest
  for i in range(len(nums)):
    heappush(maxHeap, -nums[i])

    if len(maxHeap) > k2:
      heappop(maxHeap)


  # Pop One since we don't need K2th elements for sum
  heappop(maxHeap)
  rangeSum = 0
  for _ in range(k2 - k1 - 1):
    rangeSum += -heappop(maxHeap)

  return rangeSum



def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
