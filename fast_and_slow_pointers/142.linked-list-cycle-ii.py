class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def detectCycle(head):
	##### Fast and Slow Pointer solution
	slow = head
	fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if slow == fast:
			break

	if fast == None or fast.next is None:
		return False

	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next

	return slow

	##### Value Storing Solution
	# visited = set()
	# node = head

	# while node:
	# 	if node in visited:
	# 		return node
	# 	visited.add(node)
	# 	node = node.next

	# return None

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Create a cycle

cycle_start_node = detectCycle(head)

if cycle_start_node:
    print("Cycle starts at node with value:", cycle_start_node.val)
else:
    print("No cycle in the linked list.")