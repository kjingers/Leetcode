'''
Common apprach is to use doubly linked list

    - We initialize with dummy head and tail nodes
    - When a node is put or get, we remove it and add it just after the head, so it's most recently used.
    - If we put and cache is full, we remove node before the tail and add new node after head
    
    
'''

class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
                

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
                

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
            
        node = ListNode(key, value)
        self._add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            old = self.head.next
            self._remove(old)
            del self.dict[old.key]
           
    # Adds to tail
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail
        
    # Removes Node from linked list
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
