class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def removeElements(head, val):
	dummy = ListNode(-1)
	dummy.next = head

	slow = dummy
	fast = dummy.next

	while fast:
		if fast.val is val:
			slow.next = fast.next
		else:
			slow = slow.next

		fast = fast.next

	return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None

new_head = removeElements(node1, 6)

while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
