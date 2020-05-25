class Solution:
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    self.preorder = []
    
    # get pre-order traversal
    def loop(root: TreeNode):
      if root == None:
        return
      self.preorder.append(root.val)
      loop(root.left)
      loop(root.right)

    loop(root)

    # overwrite tree nodes using pre-order traversal
    itr = root
    for val in self.preorder[1:]:
      itr.left = None
      itr.right = TreeNode(val)
      itr = itr.right

    return root
