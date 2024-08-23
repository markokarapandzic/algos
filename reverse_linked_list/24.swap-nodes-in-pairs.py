class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def swapPairs(head):
	if not head or not head.next:
		return head

	dummy = ListNode(0)
	dummy.next = head
	prev = dummy

	while prev.next and prev.next.next:
		first = prev.next
		second = prev.next.next

		prev.next = second
		first.next = second.next
		second.next = first

		prev = first

	return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

testNode = swapPairs(node1)

while testNode:
	print(str(testNode.val) + ' -> ')
	testNode = testNode.next
