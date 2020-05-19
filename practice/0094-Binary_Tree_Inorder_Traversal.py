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
  
# solved again
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    self.output = []

    def loop(root: TreeNode) -> None:
      if root == None:
        return
      loop(root.left)
      self.output.append(root.val)
      loop(root.right)

    loop(root)
    return self.output
