'''
Time O(n + nlogn) = O(nlogn)
'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
         
        # Sort by Key. Then sort by contents
        letter_logs.sort(key = lambda x : x.split()[0])
        letter_logs.sort(key = lambda x : x.split()[1:])
        
        return letter_logs + digit_logs
                         
        
