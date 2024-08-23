## ARRAY SOLUTION
# class RecentCounter:
#   def __init__(self):
#     self.requests = []
      
#   def ping(self, t: int) -> int:
#     self.requests.append(t)	

#     result = 0
#     interval = t - 3000

#     for i in range(len(self.requests) - 1, -1, -1):
#       if self.requests[i] >= interval:
#         result += 1
#       else:
#         break

#     return result

## QUEUE SOLUTION
from collections import deque

class RecentCounter:
  def __init__(self):
    self.requests = deque()
      
  def ping(self, t: int) -> int:
    self.requests.append(t)

    while self.requests[0] < t - 3000:
      self.requests.popleft()

    return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
