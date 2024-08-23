from bisect import bisect_left, bisect_right
from typing import List

def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
  start_list = sorted(f[0] for f in flowers)
  end_list = sorted(f[1] for f in flowers)

  result = []

  for time in people:
    started = bisect_right(start_list, time)
    ended = bisect_left(end_list, time)
    result.append(started - ended)

  return result

# Test the implementation with the examples provided
flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
people = [2, 3, 7, 11]
print(fullBloomFlowers(flowers, people))  # Output: [1, 2, 2, 2]

flowers = [[1, 10], [3, 3]]
people = [3, 3, 2]
print(fullBloomFlowers(flowers, people))  # Output: [2, 2, 1]
