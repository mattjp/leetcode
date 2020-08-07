# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

    # add all nodes to a priority queue, based on X-index (min heap)
    self.pq = []
    def dfs(node: TreeNode, x: int, y: int) -> None:
      if not node:
        return
      heappush(self.pq, (x, y, node.val))
      dfs(node.left, x-1, y+1)
      dfs(node.right, x+1, y+1)


    dfs(root, 0, 0)

    # for each node in the min heap, add to result set
    output = []
    while self.pq:
      # if top node has a new X-index, start a new array for the X-index
      # otherwise, continue adding to the existing X-index array
      col = []
      while self.pq and (len(col) == 0 or col[0][0] == self.pq[0][0]):
        top = heappop(self.pq)
        col.append([top[0], top[2]])

      # we only care about the value, not X-index
      output.append(list(map(lambda x: x[1], col))) 

    return output
