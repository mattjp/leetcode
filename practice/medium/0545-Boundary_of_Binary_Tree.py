class Solution:
  def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
    from collections import deque

    self.left = []
    self.right = deque()
    self.leaves = []
    self.seen = set()


    def get_left(node: TreeNode) -> None:
      if not node:
        return
      self.left.append(node)
      if node.left:
        get_left(node.left)
      elif node.right:
        get_left(node.right)


    def get_leaves(node: TreeNode) -> None:
      if not node:
        return
      if not node.left and not node.right and node not in self.seen:
        self.leaves.append(node)
      get_leaves(node.left)
      get_leaves(node.right)


    def get_right(node: TreeNode) -> None:
      if not node:
        return
      if node not in self.seen:
        self.right.appendleft(node)
      if node.right:
        get_right(node.right)
      elif node.left:
        get_right(node.left)


    if not root:
      return []
        
    get_left(root.left)
    self.seen.update(self.left)
    
    get_leaves(root)
    self.seen.update(self.leaves)
    
    get_right(root.right)
    
    r = [root.val] if root not in self.seen else []
    left = list(map(lambda x: x.val, self.left))
    leaves = list(map(lambda x: x.val, self.leaves))
    right = list(map(lambda x: x.val, self.right))
    
    return r + left + leaves + right
