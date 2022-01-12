
# My Solution
'''
def search_next_letter(letters, key):

  if len(letters) < 1:
    return None

  # If greater than largest, than return arr[0]
  if key >= letters[-1]:
    return letters[0]

  start = 0
  end = len(letters) - 1

  while start <= end:
    mid = start + (end - start) // 2

    # Return letters[mid + 1]
    # Already accounted for rollover case before loop
    if key == letters[mid]:
        return letters[mid + 1]
    
    # First Half
    if key < letters[mid]:
      end = mid - 1
    else:
      start = mid + 1
  
  return letters[start]
'''

# Solution Provided
def search_next_letter(letters, key):
  n = len(letters)

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < letters[mid]:
      end = mid - 1
    else: # key >= letters[mid]:
      start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  return letters[start % n]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
