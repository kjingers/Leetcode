def search_min_diff_element(arr, key):
  
  if key < arr[0]:
    return arr[0]
  if key > arr[-1]:
    return arr[-1]

  start, end = 0, len(arr) - 1

  while start <= end:

    mid = start + (end - start) // 2

    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      return arr[mid]

  # Here means key is not in arr
  # Since start = end + 1, compare arr[start] and arr[end]
  # arr[start] is the closest larger number
  # arr[end] is the closest smaller number
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]

  return arr[end]
