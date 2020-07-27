class Solution:
  def isSymmetric(self, root: TreeNode) -> bool:

    dq = [root] if root else []

    while dq:
      row_nodes = []

      for node in dq:
        row_nodes.append(node.left)
        row_nodes.append(node.right)

      row_vals = list(map(lambda x: x.val if x else None, row_nodes))
      m = len(row_vals) // 2
      l = row_vals[:m]
      r = list(reversed(row_vals[m:]))
      if l != r: return False

      dq = list(filter(None, row_nodes))      

    return True
