'''
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2

1: 2 - 1
2: 1 - 0
3: 3
4: 1 - 0

Time: O(n + n + n + k*logn) -> O(nlogn) worst case to construct heap
Space: O(n)

Best solution is Bucket Sort
'''
#Bucket Sort
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        
        buckets = [[] for _ in range(len(arr) + 1)]
        for key, count in counts.items():
            buckets[count].append(key)
            
        total_uniques = len(counts)
        
        for count in range(1, len(arr) + 1):
            
            # If we are looking at counts that we can't eliminate, terminate early
            if k < count:
                return total_uniques
            
            while buckets[count] and k >= count:
                k -= count
                buckets[count].pop()
                total_uniques -= 1
        
        return total_uniques
            
        
        

'''        
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        num_occurances = Counter(arr)
        
        # {5: 2, 4: 1}
        
        minHeap = [(count, num) for num, count in num_occurances.items()]
        heapify(minHeap)

        while minHeap and k > 0:
            # count = 1, num = 4
            count, num = heappop(minHeap)
            
            count -= 1
            k -= 1
            
            # count == 0
            if count > 0:
                heappush(minHeap, (count, num))
        
        return 0 if not minHeap else len(minHeap)
'''            
            
        
