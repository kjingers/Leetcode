from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
    return self.value < other.value


def merge_lists(lists):
  minHeap = []
  resultHead, resultTail = None, None
 
  # Put Head of each list into minHeap
  for root in lists:
    if root is not None:
      heappush(minHeap, root)

  # While minHeap contains nodes, pop root
  while minHeap:
    node = heappop(minHeap)

    # If resultHead is None, set resultHead
    # Else, update resultTail.next and set resultTail to current Node
    if resultHead is None:
      resultHead = node
      resultTail = node
    else:
      resultTail.next = node
      resultTail = node

    # If the corresponding list has a next, add to minHeap
    if node.next is not None:
      heappush(minHeap, node.next)
  
  return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

