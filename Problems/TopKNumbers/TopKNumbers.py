from heapq import *


def find_k_largest_numbers(nums, k):

  minHeap = []

  # First, Insert k elements to the heap
  for i in range(k):
    heappush(minHeap, nums[i])

  # Loop through the rest of the array.
  # If larger than root, then pop root and insert new num
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])

  return list(minHeap)


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

