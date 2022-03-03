'''
In first iteration, TrieNode.children is a dictionary. So, must manually add TrieNode to parent's children when inserting into Trie.


'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.trie
        
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
            
        current.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        current = self.trie
        
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        
        return current.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        
        current = self.trie
        
        for letter in prefix:
            if letter not in current.children:
                return False
            
            current = current.children[letter]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
