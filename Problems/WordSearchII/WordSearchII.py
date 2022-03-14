'''
Insert all words into Trie. Then DFS. At each cell, we will check to see if its in children of trie node. So, at each cell, we are checking the existance of all words simultaneously. Once we hit a prefix that does not exist in our trie, we backtrack and move to the next cell.
'''
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        for letter in word:
            current = current.children[letter]
        
        current.word = word
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m = len(board)
        n = len(board[0])
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        ans = []
        
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, trie.root, ans)
        
        return ans
        
        
            
    def dfs(self, board, i, j, trie_node, ans):
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in trie_node.children:
            return
        
        cell_orig = board[i][j]
        next_node = trie_node.children[cell_orig]
        
        if next_node.word != None:
            ans.append(next_node.word)
            next_node.word = None
            
            # If this letter has no children, then remove from trie
            if not next_node.children.keys():
                del trie_node.children[cell_orig]
                return
                
        board[i][j] = '#'   
            
        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            self.dfs(board, i + x, j + y, next_node, ans)
            
        # Backtrack
        board[i][j] = cell_orig
            
        
