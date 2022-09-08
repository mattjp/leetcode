# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.ans = ""
        
        def search(node):
            if not node:
                return
            
            self.ans += str(node.val)
            
            if not node.left and not node.right:
                return
            
            self.ans += "("
            search(node.left)
            self.ans += ")"
            
            # Question is stupid
            if node.right:
                self.ans += "("
                search(node.right)
                self.ans += ")"
            
        search(root)
        return self.ans
        
