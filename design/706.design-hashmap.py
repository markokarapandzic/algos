class TreeNode:
  def __init__(self, key=-1, val=1, next=None) -> None:
    self.key = key
    self.val = val
    self.next = None

class MyHashMap:
  def __init__(self):
    self.size = 10 ** 6
    self.map = [TreeNode() for _ in range(self.size)]

  def _hashKey(self, key):
    return key % self.size

  def put(self, key: int, value: int) -> None:
    currNodeHead = self.map[self._hashKey(key)]

    while currNodeHead.next:
      if currNodeHead.next.key == key:
        currNodeHead.next.val = value
        return

      currNodeHead = currNodeHead.next

    currNodeHead.next = TreeNode(key, value)

  def get(self, key: int) -> int:
    currNodeHead = self.map[self._hashKey(key)]
      
    while currNodeHead:
      if currNodeHead.key == key:
        return currNodeHead.val

      currNodeHead = currNodeHead.next

    return -1

  def remove(self, key: int) -> None:
    currNodeHead = self.map[self._hashKey(key)]

    while currNodeHead and currNodeHead.next:
      if currNodeHead.next.key == key:
        currNodeHead.next = currNodeHead.next.next
        return

      currNodeHead = currNodeHead.next

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.get(3))
print(obj.put(2, 1))
print(obj.get(2))
print(obj.remove(2))
print(obj.get(2))