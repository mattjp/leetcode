# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def widthOfBinaryTree(self, root: TreeNode) -> int:  
    deque = collections.deque([root])
    max_width = 1 if root else 0

    while deque:
      # do normal BFS, if a value is null, we must add 2 nulls in case there
      # is a row below it (since interior nulls matter)
      new_row = collections.deque()
      while deque:
        top = deque.popleft()
        if top:
          new_row.append(top.left)
          new_row.append(top.right)
        else:
          new_row.extend([None, None])

      # pop nulls from left and right
      while new_row and new_row[0] == None: new_row.popleft()
      while new_row and new_row[-1] == None: new_row.pop()

      # max local width is now the length of the new row
      max_width = max(max_width, len(new_row))

      # filter out all nulls
      vals = list(filter(lambda x: x, new_row))

      # stop iterating if all new nodes are null
      deque = new_row if vals else None

    return max_width
