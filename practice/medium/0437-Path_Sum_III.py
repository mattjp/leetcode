class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> int:

    def helper(node: TreeNode, cur: int, target: int):
      """
      recursively (DFS) find if any paths from `node` sum to `target` (top-down)
      """
      if not node:
        return
      
      cur += node.val
      
      if cur == target:
        self.output += 1
      
      helper(node.left, cur, target)
      helper(node.right, cur, target)


    def dfs(node: TreeNode):
      """
      perform pre-order traversal, checking summations at each node
      """
      if not node:
        return
      helper(node, 0, sum)
      dfs(node.left)
      dfs(node.right)


    self.output = 0      
    dfs(root)    
    return self.output
