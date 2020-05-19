# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    # idea is to iterate through preorder finding each node in inorder
    # since we know the location in inorder tells us the left/right split
    #
    # preorder         inorder
    # [3,9,10,20,15,7] [10,9,3,15,20,7]
    # [9,10,20,15,7]   [10,9]
    # [10,20,15,7]     [10]
    # [20,15,7]        [15,20,7] 
    # [15,7]           [15]
    # [7]              [7]

    self.preorder_index = 0

    def insert(inorder):
      if len(inorder) == 1:
        self.preorder_index += 1
        return TreeNode(inorder[0])
      if len(inorder) == 0:
        return None

      # create this node
      root = TreeNode(preorder[self.preorder_index])

      # find node in inorder, split left and right
      inorder_index = inorder.index(preorder[self.preorder_index])

      # add the next node
      self.preorder_index += 1

      # build children after splitting at root node
      root.left = insert(inorder[:inorder_index])
      root.right = insert(inorder[inorder_index+1:])
      return root

    return insert(inorder)
