'''
Since all boxes are the same size, we should greedy pick the boxes with the most units until the truck is full.

Similar to Knapsack problem, but all units have the same cost/weight. So, we can use greedy.

Since the box sizes are <= 1000, we can use counting sort to sort in O(1000*n) -> O(n)
'''



# Normal Sort and Greedy
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    
        totalUnits = 0
        for box in sorted(boxTypes, key=lambda x : -x[1]):
            #print(box)
            if box[0] <= truckSize:
                truckSize -= box[0]
                totalUnits += box[0] * box[1]
            else:
                totalUnits += truckSize * box[1]
                break
        
        return totalUnits
'''
    
# Counting Sort and Greedy
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        buckets = [0 for _ in range(1001)]
        totalUnits = 0
        
        for box in boxTypes:
            buckets[box[1]] += box[0]
            
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i] == 0:
                continue
            #print("Size: %d, Units: %d" % (i, buckets[i]))
            if buckets[i] <= truckSize:
                truckSize -= buckets[i]
                totalUnits += i * buckets[i]
            else:
                totalUnits += truckSize * i
                break
        
        return totalUnits
                
        
            

                
        
        
