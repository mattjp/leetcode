# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def searchBST(self, root: TreeNode, val: int) -> TreeNode:

    def search(node: TreeNode, target: int):
      if node == None:
        return None
      elif node.val == target:
        return node
      elif node.val > target:
        return search(node.left, target)
      else:
        return search(node.right, target)

    return search(root, val)
