'''
Trie Solution to quickly fine files/directories within parent directories.

Use Prefix Trie template as starting point, with search() and insert() functions

Trie Time Complexity: O(mn), where m is length of strings, and n is number of strings
'''


class TrieNode:

    def __init__(self):
        self.children = {}
        self.content = ""
        
        
class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    # Searches for path. If only prefix in trie, then returns last node of prefix.
    def search(self, path):
        
        current = self.root
        
        for word in path.split("/")[1:]:
            
            if word not in current.children:             
                return current
            
            current = current.children[word]
            
        return current
        
        
    def insert(self, path):
        
        current = self.root
        
        for word in path.split("/")[1:]:
            
            if word not in current.children:
                current.children[word] = TrieNode()
            
            current = current.children[word]
        
        return current
                
        

    def ls(self, path: str) -> List[str]:
        
        temp = [path.split("/")[-1]]
        
        node = self.search(path)
        
        # Path is a file with content. So return list with only filename
        if node.content:
            return temp
        
        # Return all files and directories in path
        return sorted(node.children.keys())
        

    def mkdir(self, path: str) -> None:
        
        self.insert(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        
        node = self.insert(filePath)
        
        node.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        
        node = self.search(filePath)
        return node.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
