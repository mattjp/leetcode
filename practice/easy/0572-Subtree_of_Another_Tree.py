# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

      # function that returns true if 2 trees are equal
      def trees_equal(a: TreeNode, b: TreeNode) -> bool:
        if a == None and b == None:
          return True
        if a == None and b != None:
          return False
        if a != None and b == None:
          return False
        if a.val != b.val:
          return False

        return trees_equal(a.left, b.left) and trees_equal(a.right, b.right)

      # DFS tree, if vals are equal, see if trees are equal
      def search(tree, subtree):
        if tree == None:
          return False
        if tree.val == subtree.val:
          if trees_equal(tree, subtree):
            return True

        return search(tree.left, subtree) or search(tree.right, subtree)

      return search(s, t)
