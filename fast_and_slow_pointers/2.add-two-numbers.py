class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def addTwoNumbers(l1, l2):
	l1_head = l1
	l2_head = l2
	new_list = ListNode(-1)
	dummy = new_list
	leader = 0

	while l2_head or l1_head:
		l1_val = l1_head.val if l1_head is not None else 0
		l2_val = l2_head.val if l2_head is not None else 0
		leader, remainder = divmod(l1_val + l2_val + leader, 10)

		new_list.next = ListNode(remainder)
		new_list = new_list.next

		l1_head = l1_head.next if l1_head else None		
		l2_head = l2_head.next if l2_head else None		

	if leader != 0:
		new_list.next = ListNode(leader)

	return dummy.next

node1 = ListNode(9)
node2 = ListNode(9)
node3 = ListNode(9)
node4 = ListNode(9)
node5 = ListNode(9)
node6 = ListNode(9)
node7 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None

node8 = ListNode(9)
node9 = ListNode(9)
node10 = ListNode(9)
node11 = ListNode(9)

node8.next = node9
node9.next = node10
node10.next = node11
node11.next = None

new_head = addTwoNumbers(node1, node4)

while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next