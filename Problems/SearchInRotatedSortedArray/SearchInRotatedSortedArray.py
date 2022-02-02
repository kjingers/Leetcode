'''
Start off binary search like normal. Calculate mid. Then, 
- Determine which side is sorted
- Check if target is in that sorted side
- If is in sorted side, shrink window to that side
- Else, shrink window to other side
'''


def search_rotated_array(arr, key):
  start, end = 0, len(arr) - 1
  
  # Start off like Normal, calculate Mid
  while start <= end:
    mid = start + (end - start) // 2

    if key == arr[mid]:
      return mid

    # If arr[mid] >= arr[start], then we know start-->mid is 
    # sorted in Ascending order.
    if arr[mid] >= arr[start]:
      
      # Now we check if key is in this range.
      if key >= arr[start] and key < arr[mid]:

        # If in this range, adjust end
        end = mid - 1

      # Else, adjust start, since we know key is in second half
      else:
        start = mid + 1

    else: # Else, mid-->end in ascending order
      
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      
      else:
        end = mid - 1

  return -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
