'''
Similar to problem, where we rearrabgle string such that no repeating characters side-by-side.

Greedy apprach. Always use character with most occurances, unless previous two chars in output are the same. Then we go with next most.


'''

from heapq import *

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        maxHeap = []
        outStr = ""        

        heappush(maxHeap, (-a, 'a'))
        heappush(maxHeap, (-b, 'b'))
        heappush(maxHeap, (-c, 'c'))
        
        while maxHeap:
            count, ch = heappop(maxHeap)
            if count == 0:
                break
            
            # If Same as previous two, need next most char
            if len(outStr) >= 2 and ch == outStr[-1] == outStr[-2]:
                
                # If no more, then must return
                if not maxHeap:
                    break
                                
                count2, ch2 = heappop(maxHeap)
                if count2 == 0:
                    break
                
                outStr += ch2

                heappush(maxHeap, (count2 + 1, ch2))
            else:
                outStr += ch
                count += 1
                

            heappush(maxHeap, (count, ch))
        
        return outStr
            
        
