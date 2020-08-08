class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:

    # in addition to root and target, we'll keep track of the closest value and its index
    def loop(root, target, index, best):
      if root == None:
          return index
      
      # compute to see which value is closest to 0
      x = float(root.val) - target
      if abs(x) < abs(best):
          best = x
          index = root.val

      # since this is a BST, we don't have to search all paths
      if target < float(root.val):
        return loop(root.left, target, index, best)
      elif target > float(root.val):
        return loop(root.right, target, index, best)
      else:
        return index

    return loop(root, target, root.val, float('-inf'))
  
# solved again
class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:

    def loop(node: TreeNode, target: float, delta: float, best: int):
      if not node:
        return best

      new_delta = abs(node.val - target)
      new_best = best
      best_delta = delta

      if new_delta < delta:
        new_best = node.val
        best_delta = new_delta

      if node.val > target:
        return loop(node.left, target, best_delta, new_best)
      elif node.val < target:
        return loop(node.right, target, best_delta, new_best)
      else:
        return new_best


    return loop(root, target, float('inf'), None)
