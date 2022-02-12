class Node:
    def __init__(self, data):
        self.child = None
        self.data = data

    def set_child(self, child):
        self.child = child

    def get_child(self):
        return self.child

    def get_data(self):
        return self.data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, data):
        self.length += 1
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.set_child(node)
            self.tail = node

    def pop(self):
        if self.head is None:
            return None
        head = self.head
        self.head = self.head.get_child()
        if self.head is None:
            self.tail = None
        self.length -= 1
        return head.get_data()
