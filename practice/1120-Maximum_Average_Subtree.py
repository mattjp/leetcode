class Solution:
  def maximumAverageSubtree(self, root: TreeNode) -> float:
    self.output = 0
    
    def dfs(node: TreeNode) -> (int, int):
      """
      return (subtree total, number of subtree items)
      """
      if not node:
        return (0, 0)
      
      l, m = dfs(node.left)
      r, n = dfs(node.right)
      
      x = (l + r + node.val)
      y = (m + n + 1)

      self.output = max(self.output, x / y)
      return (x, y)
    
    dfs(root)
    return self.output
