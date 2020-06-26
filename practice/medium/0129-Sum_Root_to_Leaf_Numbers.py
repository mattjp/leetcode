# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def sumNumbers(self, root: TreeNode) -> int:

      self.output = 0

      def find_leaf(node: TreeNode, path: List[str]) -> None:
        # catch unbalanced nodes
        if node == None:
          return

        # add leaf node and update running total
        if node.left == None and node.right == None:
          s = ''.join(path)
          s += str(node.val)
          self.output += int(s)
          return

        # add intermediate node
        path.append(str(node.val))

        # traverse left then right
        find_leaf(node.left, path)
        find_leaf(node.right, path)

        # remove intermediate node once we recurse back up
        path.pop()

      # catch empty tree
      if root != None: find_leaf(root, [])
      return self.output
