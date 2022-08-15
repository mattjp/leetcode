# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def search(node):
            """
            1. is the subtree a valid BST
            2. what is the size of the subtree
            3. return the size of the biggest valid subtree
            """
            if node == None:
                return (True, None, None, 0)
            
            # do the recursion
            valid_left, min_left, max_left, size_left = search(node.left)
            valid_right, min_right, max_right, size_right = search(node.right)
            
            # set the min/max as node val by default
            min_node = node.val
            max_node = node.val
            
            # update the smallest node seen so far
            if min_left != None:
                min_node = min(min_left, min_node)
            if min_right != None:
                min_node = min(min_right, min_node)
                
            # update the largest node seen so far
            if max_left != None:
                max_node = max(max_left, max_node)
            if max_right != None:
                max_node = max(max_right, max_node)
                
            # determine if the current node is part of a valid BST
            # valid if max left is smaller than node and min right is larger than node
            valid = (
                (node.left == None or max_left < node.val) and
                (node.right == None or min_right > node.val)
            )
            
            if valid and valid_left and valid_right:
                return (True, min_node, max_node, 1 + size_left + size_right)
            else:
                return (False, min_node, max_node, max(size_left, size_right))


        if root != None:
            _, _, _, size = search(root)
            return size
        else:
            return 0
