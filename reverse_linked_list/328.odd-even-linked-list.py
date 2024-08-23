class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def oddEvenList(head):
	if not head or not head.next:
		return head
	
	odd_head = odd = head
	even_head = even = head.next
	
	while even and even.next:
		odd.next = even.next
		odd = odd.next
		even.next = odd.next
		even = even.next
	
	odd.next = even_head
	
	return odd_head

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

testNode = oddEvenList(node1)

while testNode:
	print(str(testNode.val) + ' -> ')
	testNode = testNode.next
