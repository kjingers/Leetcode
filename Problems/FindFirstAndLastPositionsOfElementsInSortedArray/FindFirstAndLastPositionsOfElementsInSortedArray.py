'''
Very similar to a normal binary search. For this problem, we run a binary search twice to find the first and last occurrences, respectively. We do this by passing in a bool.

We will try to search for the ‘key’ in the given array; if the ‘key’ is found (i.e. key == arr[middle]) we have two options:

1. When trying to find the first position of the ‘key’, we can update end = middle - 1 to see if the key is present before middle. 
2. When trying to find the last position of the ‘key’, we can update start = middle + 1 to see if the key is present after middle.

In both cases, we will keep track of the last keyIndex found.
'''

def find_range(arr, key):
  result = [-1, -1]

  # First find first occurance
  result[0] = binary_search(arr, key, False)

  # If key exists in arr, then find last occurance
  if result[0] > -1:
    result[1] = binary_search(arr, key, True)

  return result

# If findMax, then find last occurance. Else, first occurance
def binary_search(arr, key, findMax):

  start, end = 0, len(arr) - 1

  # Default k is -1 (not in arr)
  keyIndex = -1

  while start <= end:
    mid = start + (end - start) // 2

    # First Half
    if key < arr[mid]:
      end = mid - 1
    # Second Half
    elif key > arr[mid]:
      start = mid + 1
    # Else arr[mid] == key
    else:
      keyIndex = mid
      # If we want to find the last occurance
      if findMax:
        start = mid + 1
      # If we want to find the first occurance
      else:
        end = mid - 1
        
  return keyIndex




def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()
