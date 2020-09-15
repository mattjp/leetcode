class Solution:
  def inorderSuccessor(self, node: 'Node') -> 'Node':
    """
    if node has a right - go right once, then left until None
    if node does not have a right - go up until you are the left tree of the parent node
    """  
    
    # case 1
    n = node.right
    if node.right:
      while n.left:
        n = n.left
      return n
    
    # case 2
    n = node
    while n.parent and n.parent.left != n:
      n = n.parent
    return n.parent if n else n
