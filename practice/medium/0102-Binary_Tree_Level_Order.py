# 102. Binary Tree Level-Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
      return []
    itr = [root]
    while len(itr) > 0:
      cur_res = []
      next_itr = []
      while len(itr) > 0:
        itr_top = itr.pop(0)
        cur_res.append(itr_top.val)
        if itr_top.left is not None:
            next_itr.append(itr_top.left)
        if itr_top.right is not None:
            next_itr.append(itr_top.right)
      res.append(cur_res)
      itr = next_itr
    return res
  
# solved again
class Solution:
  def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    if root == None:
      return []

    queue = collections.deque([root])
    output = collections.deque()

    while queue:
      level, next_level = [], []
      while queue:
        top = queue.popleft()
        level.append(top.val)
        if top.left: next_level.append(top.left)
        if top.right: next_level.append(top.right)
      output.appendleft(level)
      queue.extend(next_level)

    return list(output)
