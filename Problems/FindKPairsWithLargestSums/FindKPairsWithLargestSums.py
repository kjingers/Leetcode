'''
The input arrays are sorted in decending order

Similar to "Kth Smallest / Largest Numbers" Except with pair sum

We can add K pair sums + pair tuples to minHeap
For each array, need to loop from 0 to min(k, len(arr)), since the largest
K pairs are guarenteed to be made up of numbers from 0 to K

For every pair after K, we compare sum with root of minHeap
- If larger than root, pop root and push new pair
- Else, break from current inner loop, since the other numbers will only
  get smaller.
'''
from heapq import *

def find_k_largest_pairs(nums1, nums2, k):
  result = []
  minHeap = []

  for i in range(min(k, len(nums1))):
    for j in range(min(k, len(nums2))):

      # If we don't have K pairs in minHeap yet, then push
      if len(minHeap) < k:
        heappush(minHeap, (nums1[i] + nums2[j], nums1[i], nums2[j]))

      # We already have K pairs, so need to see if current pair yields a larger sum
      # than the smallest sum in the minHeap. 
      # - If so, pop root and push new pair
      # - If not, break from current inner loop, since we will only be decending
      else:
        if (nums1[i] + nums2[j]) < minHeap[0][0]:
          break
        else:
          heappop(minHeap)
          heappush(minHeap, (nums1[i] + nums2[j], nums1[i], nums2[j]))

  # At this point, our minHeap has K pairs with the largest sum. 
  # So, just need to put into result array
  for (val, num1, num2) in minHeap:
    result.append([num1, num2])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
