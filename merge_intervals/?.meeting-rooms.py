def meetingRooms(arr):
	sorted_array = sorted(arr, key=lambda x: x[0])

	for index in range(1, len(arr)):
		if sorted_array[index - 1][1] > sorted_array[index][0]:
			return False
	
	return True

print(meetingRooms([[0,30],[5,10],[15,20]])) # False
print(meetingRooms([[7,10],[2,4]])) # True