# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    from collections import deque
    
    self.parents = {}
    
    def find_parents(node: TreeNode, parent: TreeNode) -> None:
      if not node:
        return
      self.parents[node] = parent
      find_parents(node.left, node)
      find_parents(node.right, node)
      
    
    find_parents(root, None)
    output = []
    visited = set()
    queue = deque([(target, 0)])
    
    while queue:
      node, depth = queue.popleft()
      visited.add(node)
      if depth == K:
        output.append(node.val)
        
      adj_nodes = [node.left, node.right, self.parents[node]]
      for adj_node in adj_nodes:
        if adj_node and adj_node not in visited:
          queue.append((adj_node, depth + 1))
          
    return output
