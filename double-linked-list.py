class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.root = None
        self.tail = None

    def is_empty(self):
        return self.root is None # type: ignore

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.root = new_node
            self.tail = new_node
            return

        tail = self.tail

        tail.next = new_node # type: ignore
        new_node.prev = tail # type: ignore
        tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.root = new_node
            self.tail = new_node
            return

        new_node.next = self.head # type: ignore
        self.head.prev = new_node # type: ignore
        self.head = new_node

    def insert_after(self, prev_node, data):
        new_node = Node(data)
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node
        next_node.prev = new_node
        new_node.prev = prev_node

