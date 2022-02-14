'''
For each string, can use the sorted version as a key into hash map. Then append string to value.

Time Complextiy: O(nklog(k)) I think
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            
            d[key] = d.get(key, []) + [s]
            
        return list(d.values())
