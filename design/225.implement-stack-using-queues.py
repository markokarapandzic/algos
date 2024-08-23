from collections import deque

class MyStack:
  def __init__(self):
    self.q1 = deque()
    self.q2 = deque()

  def push(self, x: int) -> None:
    self.q1.append(x)

  def pop(self) -> int:
    while len(self.q1) > 1:
      self.q2.append(self.q1.popleft())

    top_element = self.q1.popleft()

    self.q1, self.q2 = self.q2, self.q1

    return top_element

  def top(self) -> int:
    while len(self.q1) > 1:
      self.q2.append(self.q1.popleft())

    top_element = self.q1.popleft()
    self.q2.append(top_element)

    self.q1, self.q2 = self.q2, self.q1

    return top_element
      
  def empty(self) -> bool:
    return not self.q1

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.push(1))
print(obj.push(2))
print(obj.top())
print(obj.push(3))
print(obj.top())
