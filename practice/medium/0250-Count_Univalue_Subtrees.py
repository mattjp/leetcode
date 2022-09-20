# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def search(node):
            if not node:
                return True
            
            l = search(node.left)
            r = search(node.right)
            
            if l and r:
                if not node.left or node.left.val == node.val:
                    if not node.right or node.right.val == node.val:
                        self.ans += 1
                        return True
            
            return False
        
        
        search(root)
        return self.ans
