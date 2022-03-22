'''
Top K Frequent Words variant?
'''

import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        
        wordList = re.findall(r'\w+', paragraph.lower())
        
        counts = Counter(w for w in wordList if w not in ban)
        
        return counts.most_common(1)[0][0]
