'''
Initialize with dictionary with words as keys and list of indices at value. The indices for each word will be in
ascending order. So, when we check shortest, we calc the distance between the first indices. Then, increment the smaller one.
'''


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = {}
        for i, w in enumerate(wordsDict):
            self.dict[w] = self.dict.get(w, []) + [i]
        
    # O(m + n), where m and n are the number of indices for words 1 and 2 respectively
    def shortest(self, word1: str, word2: str) -> int:
        i, j, = 0, 0
        l1 = self.dict[word1]
        l2 = self.dict[word2]
        minDist = float('inf')
        
        while i < len(l1) and j < len(l2):
            minDist = min(minDist, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return minDist
            
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
