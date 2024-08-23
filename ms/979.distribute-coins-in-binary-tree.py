from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def distributeCoins(self, root: Optional[TreeNode]) -> int:
    self.moves = 0		

    def dfs(node):
      if not node:
        return 0

      left_excess = dfs(node.left)
      right_excess = dfs(node.right)

      self.moves += abs(left_excess) + abs(right_excess)

      return node.val - 1 + left_excess + right_excess
    
    dfs(root)

    return self.moves

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
sol = Solution()
print(sol.distributeCoins(root))  # Output: 2

# Example 2
root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)
sol = Solution()
print(sol.distributeCoins(root))  # Output: 3
