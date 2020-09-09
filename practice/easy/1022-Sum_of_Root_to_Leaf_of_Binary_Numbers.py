# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def sumRootToLeaf(self, root: TreeNode) -> int:
    
    def dfs_and_add(node: TreeNode, number: str) -> None:
      if not node:
        return
      number += str(node.val)
      if not node.right and not node.left:
        self.numbers.append(int(number, 2))
        return
      dfs_and_add(node.left, number)
      dfs_and_add(node.right, number)
      
    
    self.numbers = []
    dfs_and_add(root, '')
    return sum(self.numbers)
        
