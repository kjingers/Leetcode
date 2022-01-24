from heapq import *

def find_Kth_smallest(matrix, k):
  minHeap = []
  count = 1

  # minHeap will contain tuple with:
  # (value, index, row)

  # Push the first element of each row into minHeap
  for row in matrix:
    if row is not None:
      heappush(minHeap, (row[0], 0, row))

  number = -1
  while minHeap:

    number, index, row = heappop(minHeap)

    if count == k:
      break
    
    count += 1

    if index + 1 < len(row):
      heappush(minHeap, (row[index + 1], index + 1, row))
  
  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
