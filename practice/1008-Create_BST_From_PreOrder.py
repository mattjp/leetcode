class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

    def insert(root: TreeNode, leaf: int) -> TreeNode:
      if root == None:
        return TreeNode(leaf)
      if root.val > leaf:
        if root.left == None:
          root.left = TreeNode(leaf)
        else:
          insert(root.left, leaf)
      else:
        if root.right == None:
          root.right = TreeNode(leaf)
        else:
          insert(root.right, leaf)
      return root

    tree = None
    for p in preorder:
      tree = insert(tree, p)
    return tree
