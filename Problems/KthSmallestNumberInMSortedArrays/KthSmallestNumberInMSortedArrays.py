from heapq import *

def find_Kth_smallest(lists, k):
  minHeap = []
  count = 1
  returnVal = -1

  # minHeap will contain tuple: (value, index into list, list)

  for i in range(len(lists)):
    if lists[i] is not None:
      heappush(minHeap, (lists[i][0], 0, lists[i]))

  while minHeap:
    val, index, list = heappop(minHeap)
    if count == k:
      returnVal = val
      break

    count += 1

    if index + 1 < len(list):
      heappush(minHeap, (list[index+1], index+1, list))

  return returnVal


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
