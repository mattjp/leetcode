# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: TreeNode) -> bool:
    
    def balance(node: TreeNode) -> (int, bool):
      if not node:
        return 0,True
      l,lb = balance(node.left)
      r,rb = balance(node.right)
      h = max(l,r)+1
      if lb and rb:
        return h, abs(l-r) <= 1
      else:
        return h,False


    return balance(root)[1]
