'''
Same idea as a normal binary search, except if the number doesn't exist in the array, 
then the index of start when the loop breaks will point to the next larger element (start = end + 1).
'''

def search_ceiling_of_a_number(arr, key):

  # If key is greater than the largest element, return -1
  if key > arr[-1]:
    return -1

  start = 0
  end = len(arr) - 1


  while start <= end:
    mid = start + (end - start) // 2

    if arr[mid] == key:
      return mid

    # First Half
    if key < arr[mid]:
      end = mid - 1
    # Second Half
    else:
      start = mid + 1
  
  return start


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
