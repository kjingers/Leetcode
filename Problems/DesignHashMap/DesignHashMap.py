'''
Straightforward solution is to calculate bucket by key % BUCKET_SIZE. Then, add (key, value), to bucket.
    - Worst case O(n) for put, get, and remove to find key in a bucket
    
Better solution is to use chaining with linked list. Still have to traverse to find key within bucket, but once found, removal is O(1)
'''

# Hash Map Implementation with Chaining
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [None for _ in range(self.bucket_size)]
        
        
    def put(self, key: int, value: int) -> None:
        bucket_index = key % self.bucket_size
        
        # If bucket is empty, then back new node as head
        if self.buckets[bucket_index] == None:
            self.buckets[bucket_index] = ListNode(key, value)
            return
        # Else, traverse list to find key. If found, update value. Else, add new node to end of list.
        else:
            previous_node = None
            current_node = self.buckets[bucket_index]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = ListNode(key, value)
        return
            # Reached end of linked list and did not find key
        

    def get(self, key: int) -> int:
        bucket_index = key % self.bucket_size
        current_node = self.buckets[bucket_index]
        
        while current_node:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next
        return -1
        

    def remove(self, key: int) -> None:
        bucket_index = key % self.bucket_size
        current_node = self.buckets[bucket_index]
        prev_node = self.buckets[bucket_index]
        
        if current_node is None:
            return
        
        # If first node in bucket, then just skip over node
        if current_node.key == key:
            self.buckets[bucket_index] = current_node.next
        else:
            current_node = current_node.next
            while current_node:
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return
                prev_node = current_node
                current_node = current_node.next
        return
                
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
