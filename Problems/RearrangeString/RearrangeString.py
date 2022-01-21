from heapq import *
from collections import Counter


def rearrange_string(str):
  # We will use a maxHeap to store the frequencies of all characters.
  # That way, we can always add the character with the highest frequency, (while avoiding dupes)

  # Pulling the character with the highest frequency gives the best chance to create a string
  # without any dupes. Greedy approach

  maxHeap = []
  resultString = []

  # Create hashmap for character and counts
  counts = Counter(str)

  # Add all to maxHeap
  for char, count in counts.items():
    heappush(maxHeap, (-count, char))

  prevChar = None
  prevCount = 0

  # Pop the char with largest frequency
  # After, put back the previous char (to avoid dupes)
  # Loop will exit when maxHeap is empty.
  while maxHeap:
    currCount, currChar = heappop(maxHeap)

    # Replace previous char. Count will be negative or 0
    if prevChar and prevCount < 0:
      heappush(maxHeap, (prevCount, prevChar))

    resultString.append(currChar)
    currCount += 1

    prevChar = currChar
    prevCount = currCount

  
  # If we exit loop but haven't appended all chars, then we were
  # unable to form a string 
  if len(resultString) == len(str):
    return ''.join(resultString)
  else:
    return ""
    



  return ""


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()

