from typing import List

class OrderedStream:
	def __init__(self, n: int):
		self.items = [None] * n
		self.index = 0

	def insert(self, idKey: int, value: str) -> List[str]:
		self.items[idKey - 1] = value	

		if idKey == self.index + 1:
			result = []

			while self.index < len(self.items) and self.items[self.index] is not None:
				result.append(self.items[self.index])
				self.index += 1

			return result

		return []

# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
print(obj.insert(3, "ccccc"))
print(obj.insert(1, "aaaaa"))
print(obj.insert(2, "bbbbb"))
print(obj.insert(5, "eeeee"))
print(obj.insert(4, "ddddd"))
