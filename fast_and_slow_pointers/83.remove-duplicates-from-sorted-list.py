class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def deleteDuplicates(head):
	if head == None or head.next == None:
		return head

	slow = head
	fast = head

	while fast:
		if slow.val == fast.val:
			slow.next = fast.next
		else:
			slow = slow.next

		fast = fast.next

	return head

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

new_head = deleteDuplicates(node1)

while new_head:
	print(new_head.val, end=" -> ")
	new_head = new_head.next