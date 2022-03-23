'''
Looks like can use Trie.

Looking at solutions, binary search is most efficient. We should:
    - With each added char, bisect_left to find insertion index
    - check 3 words to the right to see if they start with current Str
    - If they start with current string, add to temp array
    - After checking 3, add tmp array to output

Time Complexity: O(nlogn)
Space: O(logn) for sort?

Another Solution is to use Trie.
    - Each TrieNode has "suggestWord" array
    - As we add products, at each node along the way, we add to "suggestedWords" if suggestedWords < 3

''' 

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        currWord = ""
        
        for char in searchWord:
            currWord += char
            temp = []
            
            index = self.binary_search(products, currWord)
            
            for i in range(index, min(len(products), index + 3)):
                if products[i].startswith(currWord):
                    temp.append(products[i])
            
            result.append(temp)
        
        return result
            
    # bisect_left implementation
    def binary_search(self, arr, target):
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if target <= arr[mid]:
                end = mid
            else:
                start = mid + 1
        
        return start
        
        
