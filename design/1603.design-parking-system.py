class ParkingSystem:
	def __init__(self, big: int, medium: int, small: int):
		self.spaces = {}
		self.spaces[1] = big
		self.spaces[2] = medium
		self.spaces[3] = small

	def addCar(self, carType: int) -> bool:
		if self.spaces[carType] > 0:
			self.spaces[carType] -= 1
			return True

		return False

# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
