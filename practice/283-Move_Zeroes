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
