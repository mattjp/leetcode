# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Traverse the tree, keeping track of nodes seen thus far
        If no node from Root to Node is > Node, count + 1
        """
        
        self.ans = 0
        
        def search(node, max_val):
            if not node:
                return
            
            if node.val >= max_val:
                self.ans += 1
            
            search(node.left, max(max_val, node.val))
            search(node.right, max(max_val, node.val))
            
            
        search(root, root.val)
        return self.ans
