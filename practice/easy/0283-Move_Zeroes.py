class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    insertPtr: int = len(nums) - 1
    for _ in nums:
      if nums[0] == 0:
        nums.pop(0)
        nums.append(0)
        insertPtr -= 1
      else:
        nums.insert(insertPtr, nums.pop(0))
        
# solved again
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeros = len(nums)-1
    for i in range(len(nums)):
      top = nums.pop(0)
      if top == 0:
        nums.append(top)
        zeros -= 1
      else:
        nums.insert(zeros, top)
