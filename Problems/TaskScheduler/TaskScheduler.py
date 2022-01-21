from heapq import *
from collections import deque
from collections import Counter

def schedule_tasks(tasks, k):

  # We should always try to schedule the task with the highest count.
  # So, we can get the counts for each task and add to max Heap.
  # Then, pop from maxHeap to schedule (k + 1) tasks
  # For each task, add to a waitlist
  # If we cannot add (k + 1) different tasks from max heap, we need
  # to increment interval count by the difference to insert idles
  # Then, put the tasks in the waitlist back into maxHeap

  intervalCount = 0
  maxHeap = []

  # Get Counts
  counts = Counter(tasks)

  # Put into maxHeap

  for char, count in counts.items():
    heappush(maxHeap, (-count, char))


  
  while maxHeap:
    waitList = []
    # Number of different tasks to try and execute
    n = k + 1

    # Try to Execute k + 1 tasks from maxHeap
    while maxHeap and n > 0:
      count, char = heappop(maxHeap)
      #print(char, end=", ")
      count += 1
      if count < 0:
        waitList.append((count, char))
      n -= 1
      intervalCount += 1
      #print(n)
    
    # Put waitlist tasks back into maxHeap
    for count, char in waitList:
      heappush(maxHeap, (count, char))

    # If we still have tasks to execute, but haven't done k + 1 tasks this iteration,
    # then we need to increment for idle tasks
    if maxHeap:
      intervalCount += n
      #for i in range(n):
        #print("idle", end=", ")
  #print("")

  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'b', 'b', 'c', 'c'], 2)))


main()

