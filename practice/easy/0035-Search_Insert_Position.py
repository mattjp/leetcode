# 35. Insert Search Position
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in 
# order.
#
# You may assume no duplicates in the array.

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    if target in nums:
      return nums.index(target)
    i = 0
    while i < len(nums) and nums[i] < target:
      i += 1
    return i
  
# solved again using binary search
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:

    def binarySearch(nums: List[int], T: int, L: int, R: int) -> int:
      if L == R:
        if nums[L] < T:
          return L+1
        return L

      m = (L + R) // 2
      if nums[m] < T:
        return binarySearch(nums, T, m+1, R)
      elif nums[m] > T:
        return binarySearch(nums, T, L, m)
      else:
        return m

    return binarySearch(nums, target, 0, len(nums)-1)
