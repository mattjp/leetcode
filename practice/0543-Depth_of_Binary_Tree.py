class Solution:
  def depth(self, root: TreeNode) -> int:
    if root is None:
      return 0
    return max(self.depth(root.left) + 1, self.depth(root.right) + 1)

  def helper(self, root: TreeNode, largest: int) -> int:
    if root is None:
      return largest
    depth_l = self.depth(root.left)
    depth_r = self.depth(root.right)
    diameter = depth_l + depth_r
    new_largest = max(diameter, largest)
    l = self.helper(root.left, new_largest)
    r = self.helper(root.right, new_largest)
    return max(l, r)

  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    return self.helper(root, 0)
