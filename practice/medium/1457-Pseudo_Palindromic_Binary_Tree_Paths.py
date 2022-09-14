# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        Travel from root to leaf, keeping track of node values seen
        When you arrive at leaf, validate array could be a palindrome
        
        Maintain a map of {val: count}
        You may only have 1 odd count when you arrive at the leaf node
        """
        
        def update(val, amt, m, odd_count):
            m[val] += amt
            if m[val] % 2:
                odd_count += 1
            else:
                odd_count -= 1
            return odd_count
            
        
        def search(node, m, odd_count):
            if not node:
                return 0
            
            odd_count = update(node.val, 1, m, odd_count)
                
            # print(f"Node: {node.val}, M: {m}, Count: {odd_count}")
            
            if not node.left and not node.right:
                if odd_count < 2:
                    odd_count = update(node.val, -1, m, odd_count)
                    return 1
                else:
                    odd_count = update(node.val, -1, m, odd_count)
                    return 0
                
            x = search(node.left, m, odd_count) + search(node.right, m, odd_count)
            odd_count = update(node.val, -1, m, odd_count)
            return x
        
        
        return search(root, collections.defaultdict(int), 0)
