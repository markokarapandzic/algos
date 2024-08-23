class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def isPalindrome(head):
	if not head or not head.next:
		return True

	slow = head
	fast = head
	stack = []

	while fast and fast.next:
		stack.append(slow.val)
		slow = slow.next
		fast = fast.next.next

	if fast:
		slow = slow.next

	while stack:
		if stack.pop() is not slow.val:
			return False
		slow = slow.next
	
	return True

node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2
node2.next = None

print(isPalindrome(node1))
