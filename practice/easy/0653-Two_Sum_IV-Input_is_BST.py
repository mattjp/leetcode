class Solution:
  def findTarget(self, root: TreeNode, k: int) -> bool:
    
    self.seen = set()
    
    def dfs(node: TreeNode, k: int):
      if not node:
        return False
      if k-node.val in self.seen:
        return True
      self.seen.add(node.val)
      return dfs(node.left, k) or dfs(node.right, k)
    
    return dfs(root, k)
