# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    """
    take middle of nums
    create node
    set left and right recursively
    return node
    """
    
    def insert(nums: List[int], l: int, r: int) -> TreeNode:
      m = (l+r)//2
      if l == r:
        return None
      
      node = TreeNode(nums[m])
      node.left = insert(nums, l, m) 
      node.right = insert(nums, m+1, r)
      return node
      
    return insert(nums, 0, len(nums))
