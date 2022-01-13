def search_bitonic_array(arr, key):
  
  keyIndex = -1
  # First, Find Max of Bitonic Array
  maxIndex = find_max(arr)

  # Search 0 to maxIndex in Ascending order
  keyIndex = binary_search(arr, 0, maxIndex, key)

  # If not found above, search maxIndex + 1 to end in Descending Order
  if keyIndex == -1:
    keyIndex = binary_search(arr, maxIndex + 1, len(arr) - 1, key)

  return keyIndex

# Returns the index of the max element of the bitonic array
def find_max(arr):
  start, end = 0, len(arr) - 1

  while start < end:
    mid = start + (end - start) // 2

    # Descending Order
    if arr[mid] > arr[mid + 1]:
      end = mid
    # Ascending Order
    else:
      start = mid + 1

  return start

def binary_search(arr, start, end, key):
  
  while start <= end:
    mid = start + (end - start) // 2

    # If Ascending
    if arr[end] > arr[0]:
      if arr[mid] > key: # First Half
        end = mid - 1
      elif arr[mid] < key: # Second Half
        start = mid + 1
      else: # arr[mid] == key
        return mid
    else: # Descending Order
      if arr[mid] < key: # First Half
        end = mid - 1
      elif arr[mid] > key: # Second Half
        start = mid + 1
      else: # arr[mid] == key
        return mid

  return -1




def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()
