# 94. Binary Tree Inorder Traversal
# 
# Given a binary tree, return the inorder traversal of its nodes' values.

class Solution:
  def helper(self, root, x):
    if root is None:
      return x
    self.helper(root.left, x)
    x.append(root.val)
    self.helper(root.right, x)
    return x

  def inorderTraversal(self, root: TreeNode) -> List[int]:
    return self.helper(root, [])
