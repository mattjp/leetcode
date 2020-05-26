# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def binaryTreePaths(self, root: TreeNode) -> List[str]:

    self.output = []

    def loop(root: TreeNode, current: str) -> None:
      if root == None:
        return 
      if root.left == None and root.right == None:
        self.output.append(current + str(root.val))
        return

      tmp = current + str(root.val) + '->'
      loop(root.left, tmp)
      loop(root.right, tmp)

    loop(root, '')
    return self.output
