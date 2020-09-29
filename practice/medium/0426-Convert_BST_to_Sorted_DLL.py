"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
  def treeToDoublyList(self, root: 'Node') -> 'Node':
    """
    must be done in-place (otherwise would just convert to list)
    """
    
    def build(node: Node, head: Node, tail: Node) -> None:
      """
      in-order traversal, setting current node to the end of the DLL
      """
      if not node:
        return
      
      build(node.left, head, tail)
      
      # insert `node` into the last spot in the DLL (pointing to `tail`)
      node.left = tail.left
      tail.left.right = node
      tmp = node.right # save node.right, before overwrite
      node.right = tail
      tail.left = node
      
      build(tmp, head, tail)


    # init head + tail nodes
    head = Node(0)
    tail = Node(0)
    head.right = tail
    tail.left = head
    
    build(root, head, tail)
    
    # make the DLL circular
    head.right.left = tail.left
    tail.left.right = head.right
    return head.right if head.right != tail else None
