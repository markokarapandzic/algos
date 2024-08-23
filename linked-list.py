class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return

        current = self.head

        while current.next: # type: ignore
            current = current.next # type: ignore

        current.next = new_node # type: ignore

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head # type: ignore
        self.head = new_node

    def insert_after(self, prev_node, data):
        new_node = Node(data)
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node

    def delete(self, key):
        current = self.head
        prev = None

        while current.data != key: # type: ignore
            prev = current
            current = current.next # type: ignore

        prev.next = current.next # type: ignore

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.insert_after(linked_list.head, 15)
linked_list.delete(20)
linked_list.print_list()

