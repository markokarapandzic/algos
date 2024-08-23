class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def middleNode(head):
	if head is None:
		return None

	if head.next is None:
		return head

	slow = head
	fast = head

	while fast.next:
		slow = slow.next

		if fast.next.next is not None:
			fast = fast.next.next
		else:
			fast = fast.next

	return slow

node1 = ListNode(1)

node1.next = None

print(middleNode(node1))
