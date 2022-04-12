'''
Example: 
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]

Output: 5 -- "hit" -> "hot" -> "dot" -> "dog" -> "cog"

"Shortest" transformation sequence makes me think BFS

For each word, there are 26 * len(word) potential neighbors. We check to see if any of these potential neighbors are in the word list. If so, remove from list and add to queue.

Once we get to the endWord, we know we are at the shortest distance given we are using BFS.
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        setList = set(wordList)
        
        if endWord not in setList:
            return 0
        
        queue = deque([beginWord])
        res = 1
        
        while queue:
            
            for _ in range(len(queue)):
                currWord = queue.popleft()

                if currWord == endWord:
                    return res

                for i in range(len(currWord)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        tempWord = currWord[:i] + j + currWord[i+1:]
                        if tempWord in setList:
                            queue.append(tempWord)
                            setList.remove(tempWord)
            
            res += 1
        
        return 0
                
        
        
