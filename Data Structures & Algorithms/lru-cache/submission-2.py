class Node:
    def __init__(self, key: int, value:int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.L = Node(0,0)
        self.R = Node(0,0)
        self.L.right = self.R
        self.R.left = self.L

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key]
            self.cache[key].left.right = self.cache[key].right
            self.cache[key].right.left = self.cache[key].left

            self.cache[key].left = self.R.left
            self.cache[key].right = self.R
            self.R.left.right = self.cache[key]
            self.R.left = self.cache[key]

            return self.cache[key].value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].left.right = self.cache[key].right
            self.cache[key].right.left = self.cache[key].left

            self.cache[key].left = self.R.left
            self.cache[key].right = self.R
            self.R.left.right = self.cache[key]
            self.R.left = self.cache[key]

            self.cache[key].value = value

        else:
            self.cache[key] = Node(key,value)
            temp = self.R.left
            self.R.left = self.cache[key]
            self.cache[key].left = temp
            temp.right = self.cache[key]
            self.cache[key].right = self.R

        if len(self.cache) > self.capacity:
            lru = self.L.right
            self.L.right = self.L.right.right
            self.L.right.left = self.L
            del self.cache[lru.key]
            
        
