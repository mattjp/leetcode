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
