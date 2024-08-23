class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def rotateRight(head, k):
	if not head or not head.next or k == 0:
		return head

	length = 1
	curr = head

	while curr.next:
		curr = curr.next
		length += 1

	curr.next = head
	rotatio_point = length - k % length

	new_tail = head
	for _ in range(rotatio_point - 1):
		new_tail = new_tail.next

	new_head = new_tail.next
	new_tail.next = None

	return new_head

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

testNode = rotateRight(node1, 2)

while testNode:
	print(str(testNode.val) + ' -> ')
	testNode = testNode.next
