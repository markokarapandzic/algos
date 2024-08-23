class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def merge_sort(head):
	if not head or not head.next:
		return head
	
	slow = head
	fast = head.next

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	
	second_half = slow.next
	slow.next = None
	
	sorted_first_half = merge_sort(head)
	sorted_second_half = merge_sort(second_half)
	
	return merge(sorted_first_half, sorted_second_half)

def merge(l1, l2):
	dummy = ListNode()
	current = dummy
	
	while l1 and l2:
		if l1.val < l2.val:
			current.next = l1
			l1 = l1.next
		else:
			current.next = l2
			l2 = l2.next
		current = current.next
	
	current.next = l1 if l1 else l2
	
	return dummy.next

def sort_linked_list(head):
  return merge_sort(head)

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

sorted_head = sort_linked_list(head)

while sorted_head:
    print(sorted_head.val, end=" -> ")
    sorted_head = sorted_head.next
