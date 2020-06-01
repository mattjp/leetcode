class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:

    def loop(root):
      if root == None:
        return None
      l = loop(root.left)
      r = loop(root.right)
      root.left = r
      root.right = l
      return root

    return loop(root)
