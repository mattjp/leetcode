# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    
    def dfs(node: TreeNode, target: int, cur: int=0, path: List[int]=[], output: List[List[int]]=[]):
      if not node:
        return output
      if not node.left and not node.right:
        if cur+node.val == target:
          output.append(path+[node.val])
        return output
      
      path.append(node.val)
      output = dfs(node.left, target, cur+node.val, path)
      output = dfs(node.right, target, cur+node.val, path)
      path.pop()
      return output
    
    return dfs(root, sum)
