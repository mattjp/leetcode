class Solution:
  def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    """
    - if node exists
    - save left node as `tmp`
    - target node becomes right node
    - follow new node left until None
    - set left to `tmp`
    """


    def delete_if_found(node: TreeNode) -> TreeNode:
      if not node:
        return None
      if node.val == key:
        # save old nodes
        old_left = node.left
        old_right = node.right

        # search for left-most node in right sub-tree, if there is a right sub-tree
        bottom_left = node.right
        if bottom_left:
          node = old_right

          # keep going left
          # invariant will hold because it's a BST
          while bottom_left.left:
            bottom_left = bottom_left.left

          # current node becomes right node
          bottom_left.left = old_left

        # there's nothing in the right sub-tree
        else:
          node = old_left  

      elif node.val > key:
        node.left = delete_if_found(node.left)
      else:
        node.right = delete_if_found(node.right)

      # always return `node` to "rebuild" the tree
      return node

    return delete_if_found(root)
