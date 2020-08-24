# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    self.output = 0

    def loop(node: TreeNode, prev: str):
      if not node: 
        return
      loop(node.left, 'L')
      loop(node.right, 'R')
      if prev == 'L' and not node.left and not node.right:
        self.output += node.val

    loop(root, '')
    return self.output
