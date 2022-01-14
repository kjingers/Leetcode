'''
We want to find the pivot point.
'''


def count_rotations(arr):
  
  # Start Binary Search as Normal
  start, end = 0, len(arr) - 1

  while start < end:
    mid = start + (end - start) // 2

    # Compare arr[mid] with numbers on both sides
    # Use mid < end and mid > start to avoid comparing beyond index
    # of current search range
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1
    elif mid > start and arr[mid] < arr[mid - 1]:
      return mid

    # Now, we need to see which side is sorted
    # Pivot point will be on the non-sorted side
    if arr[mid] >= arr[start]:
      start = mid + 1
    else:
      end = mid - 1

  # If we get to here, then no pivot point found
  return 0


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
