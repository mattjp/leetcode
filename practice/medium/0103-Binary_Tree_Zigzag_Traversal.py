# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    # stupid error checking
    if root == None:
      return []

    output = [[root.val]]
    stack = [root]
    while len(stack) > 0:
      current = []
      for s in stack:
        if s.left != None:
          current.append(s.left)
        if s.right != None:
          current.append(s.right)
      if len(current) > 0:
        output.append(list(map(lambda x: x.val, current))) # append vals
    stack = current

    # there has to be a better way of doing this
    for i,o in enumerate(output):
      if i % 2 == 1:
        o.reverse()
    return output
  
# solved again
class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

    if not root: return [] # i hate error checking

    output = []
    dq = collections.deque([root])
    direction = 1

    while dq:
      next_row = collections.deque()
      output.append(list(map(lambda x: x.val, dq))) # only take node values
      
      while dq:
        top = dq.pop() # always pop from left, since nodes are added in correct order
        if direction == 1:
          if top.right: next_row.append(top.right)
          if top.left:  next_row.append(top.left)
        else:
          if top.left:  next_row.append(top.left)
          if top.right: next_row.append(top.right)

      dq = next_row
      direction *= -1 # add nodes in the opposite direction for the next row

    return output
