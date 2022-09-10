# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        1. Flatten and swap until everything is sorted
        """
        
        def in_order(node, nodes):
            if not node:
                return nodes
            nodes = in_order(node.left, nodes)
            nodes.append(node)
            nodes = in_order(node.right, nodes)
            return nodes
        
        nodes = in_order(root, [])
        
        # Given a sorted list with 2 elements swapped, put the list back in order
        a = b = 0
        for i in range(len(nodes)-1):
            # Iterate until we find non-increasing elements
            if nodes[i].val > nodes[i+1].val:
                a = i
                b = i+1
                # Iterate until the new index has been found
                while b < len(nodes) and nodes[a].val > nodes[b].val:
                    b += 1

                # Swap and exit
                nodes[a].val, nodes[b-1].val = nodes[b-1].val, nodes[a].val
                break
