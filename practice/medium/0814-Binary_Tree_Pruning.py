# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        if the sum of the L/R subtree is 0, set L/R = None
        """
        
        def search(node):
            if not node:
                return 0
            
            l = search(node.left)
            r = search(node.right)
            
            if l == 0:
                node.left = None
            if r == 0:
                node.right = None

            return l + r + node.val
        
        # Run the damn ball
        search(root)
        
        # Stupid edge cases
        if not root:
            return root
        elif not root.left and not root.right and root.val == 0:
            return None
        else:
            return root        
        
