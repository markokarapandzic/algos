def merge(intervals):
	if not intervals:
		return []

	intervals.sort(key=lambda x: x[0])
	stack = [intervals[0]]

	for index in range(1, len(intervals)):
		if stack[-1][1] >= intervals[index][0]:
			stack[-1][1] = max(stack[-1][1], intervals[index][1])
		else:
			stack.append(intervals[index])

	return stack

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[5,6]]))
print(merge([[1,4],[0,4]]))
print(merge([[1,4],[2,3]]))
