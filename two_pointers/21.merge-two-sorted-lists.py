class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def mergeTwoLists(list1, list2):
	dummy = head = ListNode(0)

	while list1 and list2:
		if list1.val < list2.val:
			head.next = list1
			list1 = list1.next
		else:
			head.next = list2
			list2 = list2.next
		head = head.next

	head.next = list1 or list2

	return dummy.next
	
# EXAMPLES =======================================================================
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4) # [1,2,4]

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4) # [1,3,4]

merged_list = mergeTwoLists(list1, list2) # 1,1,2,3,4

while merged_list:
	print(merged_list.val, end=" -> ")
	merged_list = merged_list.next

# Example 2
list1 = None
list2 = None

merged_list = mergeTwoLists(list1, list2)

if not merged_list:
	print("NULL")

# Example 3
list1 = None
list2 = ListNode(0)

merged_list = mergeTwoLists(list1, list2)

while merged_list:
	print(merged_list.val, end=" -> ")
	merged_list = merged_list.next

print("NULL")
