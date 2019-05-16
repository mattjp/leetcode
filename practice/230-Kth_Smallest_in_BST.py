# 230. Kth Smallest Element in a Binary Search Tree
# 
# Given a binary search tree, write a function kthSmallest to find the kth 
# smallest element in it.
#
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    q = [root]
    v = []
    while len(q) > 0:
      top = q.pop()
      v.append(top.val)
      if top.right is not None:
        q.append(top.right)
      if top.left is not None:
        q.append(top.left)
    v.sort()
    return v[k-1]
