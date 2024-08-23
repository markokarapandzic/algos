def intervalIntersection(firstList, secondList):
	result = []
	first = second = 0

	while first < len(firstList) and second < len(secondList):
		start1, end1 = firstList[first]
		start2, end2 = secondList[second]

		if start1 <= end2 and start2 <= end1:
			intersection_start = max(start1, start2)
			intersection_end = min(end1, end2)
			result.append([intersection_start, intersection_end])

		if end1 <= end2:
			first += 1
		else:
			second += 1

	return result

print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(intervalIntersection([[1,3],[5,9]], []))
