'''
Pretty much a normal Binary Search.
Except a key, we narrow min down to the max element

1. If mid is in the decreasing portion, then set end = mid
2. If mid is in the increasing portion, then set start = mid + 1

When loop ends, start == end, both index of max element
'''

def find_max_in_bitonic_array(arr):
  
  start, end = 0, len(arr) - 1

  while start < end:
    mid = start + (end - start) // 2
    # Max index is <= mid
    if arr[mid] > arr[mid + 1]:
      end = mid
    # Max index is > mid
    else:
      start = mid + 1

  # When We break from loop, start == end
  # Both are index of max element
  return arr[start]



def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()
