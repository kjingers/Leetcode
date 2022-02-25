'''
Greedy, similar to Jump Game II and Number Of Taps

    - Can create array where index is the start of a clip, and right is the max
      end of a clip that starts at that index
      
    - Then, can Greedily pick the biggest start within each range
'''

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        clipMax = [0 for i in range(101)]
        
        for clip in clips:
            clipMax[clip[0]] = max(clipMax[clip[0]], clip[1])
            
        start, end = 0, 0
        numClips = 0
        
        while end < time:
            
            maxEnd = max([clipMax[i] for i in range(start, end + 1)])
            start = end
            end = maxEnd
            
            numClips += 1
            
            if end <= start:
                return -1
            
        return numClips
        
