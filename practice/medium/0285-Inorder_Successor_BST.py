# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    
    def search(node: TreeNode, best: TreeNode, target: int) -> TreeNode:
      if not node:
        return best  
      elif node.val <= target:
        return search(node.right, best, target)
      else:
        best = best if best and best.val < node.val else node
        return search(node.left, best, target)
        
    return search(root, None, p.val)
