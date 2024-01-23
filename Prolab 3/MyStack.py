class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        current_node = self.top
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count