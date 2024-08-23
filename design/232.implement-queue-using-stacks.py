class MyQueue:
  def __init__(self):
    self.stack1 = []	
    self.stack2 = []

  def _swap(self):
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())

  def push(self, x: int) -> None:
    self.stack1.append(x)	

  def pop(self) -> int:
    self._swap()
    return self.stack2.pop()

  def peek(self) -> int:
    self._swap()
    return self.stack2[-1]

  def empty(self) -> bool:
    return not self.stack1 and not self.stack2

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())
