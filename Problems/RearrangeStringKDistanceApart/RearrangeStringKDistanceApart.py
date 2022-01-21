from heapq import *
from collections import Counter
from collections import deque

def reorganize_string(str, k):
  # Similar to Rearrange String

  # Store all char in maxHeap by freq
  # Use greedy approach to append char with highest freq
  # Put the currentChar and currFreq in queue
  # Once K has passed, pop from queue and put back in heap

  # If k < 2, then we can have the same string
  if k < 2:
    return str

  maxHeap = []
  resultString = []
  charQueue = deque()

  counts = Counter(str)

  for char, count in counts.items():
    heappush(maxHeap, (-count, char))


  prevChar, prevCount = None, 0
  i = 0
  while maxHeap:

    # Pop and append to result string
    currCount, currChar = heappop(maxHeap)
    resultString.append(currChar)

    # Decrement Count and append to queue
    charQueue.append((currCount + 1, currChar))
    i += 1

    # If we've done k iterations, pop from queue
    # This is the char that we appended k iterations ago
    if i >= k:
      prevCount, prevChar = charQueue.popleft()
      if prevCount < 0:
        heappush(maxHeap, (prevCount, prevChar))


  return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()
