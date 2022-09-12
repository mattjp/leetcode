# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def collect(node, leaves):
            if not node:
                return False, leaves
            
            if not node.left and not node.right:
                leaves.append(node.val)
                return True, leaves
            
            l_leaf, leaves = collect(node.left, leaves)
            r_leaf, leaves = collect(node.right, leaves)
            
            if l_leaf:
                node.left = None
            if r_leaf:
                node.right = None
                
            return False, leaves
        
        ans = []
        is_leaf = False
        while not is_leaf:
            is_leaf, leaves = collect(root, [])
            ans.append(leaves)
            
        return ans
        
