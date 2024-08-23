from collections import defaultdict

def numOfMinutes(n, headID, manager, informTime):
  tree = defaultdict(list)

  for i in range(n):
    if manager[i] != -1:
      tree[manager[i]].append(i)

  def dfs(node):
    if node not in tree:
      return 0

    max_min = 0

    for child in tree[node]:
      max_min = max(max_min, dfs(child))

    return max_min + informTime[node]
  
  return dfs(headID)


print(numOfMinutes(1, 0, [-1], [0]))
print(numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
