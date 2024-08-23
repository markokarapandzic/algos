class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def reverseList(head, left, right):
	prev = None
	curr = head
	index = 1

	while index <= right + 1:
		if index >= left and index <= right:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next

		index += 1

	return prev

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

testNode = reverseList(node1, 2, 4)

while testNode:
	print(str(testNode.val) + ' -> ')
	testNode = testNode.next
