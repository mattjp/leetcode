"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
  def connect(self, root: 'Node') -> 'Node':
    queue = [root]
    
    while queue:
      children = []
      for node in queue: # normal BFS
        if not node:
          continue
        if node.left:
          children.append(node.left)
        if node.right:
          children.append(node.right)
          
      for i in range(len(children)-1): # for this row of children, update next pointers
        children[i].next = children[i+1]

      queue = children
      
    return root
