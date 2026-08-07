class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.mp = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        # check if key exists in the map
        # yes -> REMOVE the old node and INSERT it to the end of the linkedlist
        #       update the map with the new node
        #       return the vlaue
        # no -> return -1
        

    def put(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if key in self.mp:
            node = self.mp[key]
            self.remove(node)
            self.insert(newNode)
            self.mp[key] = newNode
        else:
            self.insert(newNode)
            self.mp[key] = newNode
            self.size += 1
            if self.size > self.capacity:
                rNode = self.left.next
                self.remove(rNode)
                del self.mp[rNode.key]
        # check if key exists in map
            # yes -> REMOVE the old node and INSERT it to the end of the linkedlist
            #       update the map key with the new node
            # no -> INSERT a new node to the right of the linkedlist and increment the size, 
            #       if the size is greater that capacity, REMOVE the left node
            #       add the new node ot the map
            #       delete the removed node from the map
        
