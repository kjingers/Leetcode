'''
When organizing the string, putting the most frequent letter gives us the best change to return a string with so repeating characters. So greeedy approach works. Once we count occurances, then use maxHeap to always access most occuring letter.
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        letter_counts = Counter(s)
        
        max_heap = []
        output_list = []
        
        for letter, count in letter_counts.items():
            heappush(max_heap, (-count, letter))
            
        prev_count = -1
        prev_letter = ""
        
        while max_heap:
            count, letter = heappop(max_heap)
            
            output_list.append(letter)
            
            if prev_count < -1:
                heappush(max_heap, (prev_count + 1, prev_letter))
                
            prev_count = count
            prev_letter = letter
            
            
        return ''.join(output_list) if len(output_list) == len(s) else ""
            
            
            
            
            
        
        
