# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

    def loop(a: TreeNode, b: TreeNode):
      if not a and not b:
        return True
      elif (
        a and not b
        or b and not a
        or a.val != b.val
      ):
        return False
      
      return loop(a.left, b.left) and loop(a.right, b.right)
    
    return loop(p, q)
