# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def isValidBST(self, root: TreeNode) -> bool:

    self.inorder = [] # save in-order traversal

    def loop(root: TreeNode) -> None:
      if root == None:
        return
      loop(root.left)
      self.inorder.append(root.val)
      loop(root.right)

    loop(root)

    for i in range(len(self.inorder)-1):
        if self.inorder[i] >= self.inorder[i+1]: # assert in-order traversal is strictly ascending
            return False
    return True
