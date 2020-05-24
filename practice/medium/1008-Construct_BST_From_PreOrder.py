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
  
# solved again
class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

    # function for inserting a node
    def insert(root: TreeNode, val: int) -> TreeNode:
      if root == None:
        return TreeNode(val)

      if val < root.val:
        root.left = insert(root.left, val)
      else:
        root.right = insert(root.right, val)
      return root

    root = None

    # since we're given pre-order, we know the first element is the root
    # from there we can just insert into the BST like normal
    for val in preorder:
      root = insert(root, val)

    return root
