class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # left = least recently used
        # right = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """
        Remove node from its current position in the linked list.
        """
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        """
        Insert node just before right dummy node.
        This makes it the most recently used item.
        """
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        next_node.prev = node

        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # mark as recently used
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            # remove least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
