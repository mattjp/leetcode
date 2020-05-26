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
  
  # solved again using recursion
class Solution:
  def flatten(self, root: TreeNode) -> None:
  """
  Do not return anything, modify root in-place instead.
  """

  def loop(root: TreeNode) -> TreeNode:
    if root == None:
      return None
    if root.right == None and root.left == None:
      return root

    l_tail = loop(root.left) # 
    r_tail = loop(root.right)

    # reorder the current subtree
    if l_tail != None:
      l_tail.right = root.right # left tail must point to current left
      root.right = root.left # swap right in for left
      root.left = None

    # return the deepest node coming from the left subtree
    return r_tail if r_tail != None else l_tail

  # do work
  loop(root)
