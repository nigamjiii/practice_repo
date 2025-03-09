class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {}

    def _remove_node(self, node: Node):
        """Remove a node from its current position."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node_to_front(self, node: Node):
        """Add a node right after the head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        temp = self.hash_map[key]
        # Move the accessed node to the front
        self._remove_node(temp)
        self._add_node_to_front(temp)

        return temp.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # Update the value of the existing node and move it to the front
            temp = self.hash_map[key]
            temp.value = value
            self._remove_node(temp)
            self._add_node_to_front(temp)
        else:
            if len(self.hash_map) == self.size:
                # Remove the least recently used node (node before the tail)
                to_remove = self.tail.prev
                self._remove_node(to_remove)
                del self.hash_map[to_remove.key]

            # Add the new node to the front
            new_node = Node(key, value)
            self._add_node_to_front(new_node)
            self.hash_map[key] = new_node

link = 'https://leetcode.com/problems/lru-cache/'