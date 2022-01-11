'''
This is from Grokking, where the sorted array could be ascending or decending order
'''

def binary_search(arr, key):
  start = 0
  end = len(arr) - 1
  isAscending = arr[end] > arr[start]

  while end >= start:
    mid = start + (end - start) // 2

    if arr[mid] == key:
      return mid
    
    if isAscending:
      # In first half
      if key < arr[mid]:
        end = mid - 1
      # In second half
      else:
        start = mid + 1
    else:
      # In first half
      if key > arr[mid]:
        end = mid - 1
      # In second half
      else:
        start = mid + 1

  return -1


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()
