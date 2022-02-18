# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Need to convert tree into a serialized string. So, need a way to put tree into string, so that it can be parsed out
node by node and account for NULL (no left/right children).

Will Try Preorder representation sing BFS.

The main idea is to put the node values in a list. Then, to deserialize, maintain an index i into the list
to keep track of the next child.
'''
from collections import deque

class Codec:

    def serialize(self, root):
        
        queue = deque()
        ser = []
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                ser.append("#")
                ser.append(",")
                continue
            
            ser.append(str(node.val))
            ser.append(",")
            
            queue.append(node.left)
            queue.append(node.right)
        
        s = ''.join(ser)
        t = s.split(',')
        print(t)
        return ''.join(ser)
            
                

    def deserialize(self, data):
        
        ser = data.split(',')
        
        queue = deque()
        
        if ser[0] == '#':
            return None
        
        root = TreeNode(int(ser[0]))
        queue.append(root)
        i = 1
        
        while queue:
            
            node = queue.popleft()
            
            if ser[i] == '':
                break
            
            # If not null, make left child and put into queue
            if ser[i] != '#':
                node.left = TreeNode(int(ser[i]))
                queue.append(node.left)
                
            i += 1
            
            # If not null, make right child and put into queue
            if ser[i] != '#':
                node.right = TreeNode(int(ser[i]))
                queue.append(node.right)
                
            i += 1
            
        return root
                        
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
