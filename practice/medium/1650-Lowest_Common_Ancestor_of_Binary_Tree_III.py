"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        BFS from one node until the other is reached
        Remember the highest node seen at the current node
        """
        
        visited = set()
        queue = collections.deque([(p, p)])
        
        while queue:
            cur, ancestor = queue.popleft()
            
            if cur == q:
                return ancestor
            
            visited.add(cur)
            
            if cur.left and cur.left not in visited:
                queue.append((cur.left, ancestor))
            
            if cur.right and cur.right not in visited:
                queue.append((cur.right, ancestor))
                
            if cur.parent and cur.parent not in visited:
                queue.append((cur.parent, cur.parent))
                
        return None
