# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
    def dfs(node: TreeNode, target: int, cur: int):
      if not node:
        return False
      if not node.left and not node.right:
        return (cur+node.val) == target
      return dfs(node.left, target, cur+node.val) or dfs(node.right, target, cur+node.val)
    
    return dfs(root, sum, 0) if root else False
