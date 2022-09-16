# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
        For each node, what's the max length of each child node?
        Is the current node exactly 1 greater than either child?
        """
        
        self.ans = 0
        
        # Return (length, value)
        def search(node):
            if not node:
                return 0, None
            
            len_l, val_l = search(node.left)
            len_r, val_r = search(node.right)
            
            max_l = 0
            max_r = 0
            
            if val_l != None and node.val + 1 == val_l:
                max_l = len_l
                    
            if val_r != None and node.val + 1 == val_r:
                max_r = len_r
                    
            # print(f"Node: {node.val}, valL: {val_l}, valR: {val_r}")
                   
            # We can do 1 better than the best L/R child
            best = 1 + max(max_l, max_r)
            
            # Update global variable
            self.ans = max(self.ans, best)
            return best, node.val
          
          
        search(root)
        return self.ans
