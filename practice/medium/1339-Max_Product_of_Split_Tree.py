# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        All we can do is remove 1 edge
        Therefore, at each node we can calculate the max product for
            left edge removed
            right edge removed
            
        At each node, the 2 subtrees will be
            Either the left or right subtree
            The current node 
                plus either the left or right subtree
                plus everything above the current node
                
        Get the entire sum of the tree
        At each node, (sum-sum_sub_tree)*(sum_sub_tree)
        Return the sum of the left and right sub trees
        """


        def get_sum(node):
            if node == None:
                return 0
            return get_sum(node.left) + node.val + get_sum(node.right)
        
        
        def get_subtree_sum(node, tree_sum):
            if node == None:
                return 0
            
            # get the sum of the left and right subtrees
            l_sum = get_subtree_sum(node.left, tree_sum)
            r_sum = get_subtree_sum(node.right, tree_sum)
            
            # calculate the product if we removed the left or right edge
            l = (tree_sum - l_sum) * l_sum
            r = (tree_sum - r_sum) * r_sum
            
            # take the best option we've seen thus far
            self.best = max(self.best, l, r)
            
            # return the sum of the subtrees
            return l_sum + node.val + r_sum
            

        self.best = 0  # global ha ha
        
        tree_sum = get_sum(root)
        
        get_subtree_sum(root, tree_sum)
        
        return (self.best % 1_000_000_007)
