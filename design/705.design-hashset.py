## List Node Solution
class ListNode:
  def __init__(self, key) -> None:
    self.key = key
    self.next = None

class MyHashSet:
  def __init__(self):
    self.set = [ListNode(0) for _ in range(10 ** 4)]	

  def add(self, key: int) -> None:
    currNode = self.set[key % len(self.set)]

    while currNode.next:
      if currNode.next.key == key:
        return

      currNode = currNode.next

    currNode.next = ListNode(key)

  def remove(self, key: int) -> None:
    currNode = self.set[key % len(self.set)]

    while currNode.next:
      if currNode.next.key == key:
        currNode.next = currNode.next.next
        return

      currNode = currNode.next

  def contains(self, key: int) -> bool:
    currNode = self.set[key % len(self.set)]

    while currNode.next:
      if currNode.next.key == key:
        return True

      currNode = currNode.next

    return False

## ARRAY SOLUTION
# class MyHashSet:
# 	def __init__(self):
# 		self.size = 10 ** 4
# 		self.set = [[] for _ in range(self.size)]	

# 	def _hash(self, key):
# 		return key % self.size

# 	def add(self, key: int) -> None:
# 		hashKey = self._hash(key)	

# 		if not self.contains(key):
# 			self.set[hashKey].append(key)

# 	def remove(self, key: int) -> None:
# 		hashKey = self._hash(key)	

# 		if not self.contains(key):
# 			self.set[hashKey].remove(key)

# 	def contains(self, key: int) -> bool:
# 		hashKey = self._hash(key)
# 		return key in self.set[hashKey]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))