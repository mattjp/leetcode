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
    if root == None:
      return None

    s2 = [root]

    while len(s2) > 0:
      s1 = s2.copy()
      s2 = []
      while len(s1) > 0:
        top = s1.pop(0)
        top.next = s1[0] if len(s1) > 0 else None 
        if top.left != None and top.right != None:
          s2.extend([top.left, top.right])

    return root
