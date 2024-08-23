class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def hasCycle(head):
	if not head or head.next is None:
		return False

	slow_p = head
	fast_p = head.next

	while fast_p and fast_p.next:
		if slow_p == fast_p:
			return True
		
		slow_p = slow_p.next
		fast_p = fast_p.next.next
	
	return False

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node3

print(hasCycle(node1))

node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2
node2.next = None

print(hasCycle(node1))
print(hasCycle(None))

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

print(hasCycle(node1))
