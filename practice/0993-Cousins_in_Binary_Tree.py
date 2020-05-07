# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

    def getDepth(root: TreeNode, t: int, depth: int) -> int:
      if root == None:
        return -1
      if root.val == t:
        return depth
      l = getDepth(root.left, t, depth+1)
      if l != -1:
        return l
      r = getDepth(root.right, t, depth+1)
      return r

    def getParent(root: TreeNode, parent: TreeNode, t: int) -> TreeNode:
      if root == None:
        return None
      if root.val == t:
        return parent
      l = getParent(root.left, root, t)
      if l != None:
        return l
      r = getParent(root.right, root, t)
      return r

    x_depth = getDepth(root, x, 0)
    y_depth = getDepth(root, y, 0)
    if x_depth != y_depth:
      return False

    x_parent = getParent(root, None, x)
    y_parent = getParent(root, None, y)
    if x_parent == y_parent:
      return False
    return True
