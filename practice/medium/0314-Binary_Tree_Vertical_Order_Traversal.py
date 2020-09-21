class Solution:
  def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    from collections import defaultdict, deque
    
    queue = deque([(root, 0)]) if root else deque()
    cols = defaultdict(list)
    
    while queue:
      node, col = queue.popleft()
      cols[col].append(node.val)
      if node.left:
        queue.append((node.left, col-1))
      if node.right:
        queue.append((node.right, col+1))
        
    # sorting is dumb. instead, we could get the min and max column of the
    # binary tree by doing a DFS first, then iterating from min-col to max-col
    return list(map(lambda x: x[1], sorted(cols.items())))
