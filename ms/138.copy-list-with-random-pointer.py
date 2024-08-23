from typing import Optional

class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
	if not head:
		return []

	old_to_new = {}

	current = head
	while current:
		old_to_new[current] = Node(current.val)
		current = current.next

	current = head
	while current:
		if current.next:
			old_to_new[current].next = old_to_new[current.next]
		if current.random:
			old_to_new[current].random = old_to_new[current.random]
		current = current.next

	return old_to_new[head]

def printLinkedList(head):
	nodes = []
	while head:
		random_val = head.random.val if head.random else None
		nodes.append(f"[{head.val}, {random_val}]")
		head = head.next
	print(" -> ".join(nodes))

# Example usage
# Create a linked list [[7,null],[13,0],[11,4],[10,2],[1,0]]
original = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
original.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node2.random = original
node3.random = node5
node4.random = node3
node5.random = original

# Deep copy the list
copied_list = copyRandomList(original)
printLinkedList(copied_list)
