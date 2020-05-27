class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    i = 1
    while i < len(nums) and nums[i] >= nums[i-1]:
        i += 1
    return i-1
