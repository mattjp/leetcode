# 189. Rotate Array
#
# Given an array, rotate the array to the right by k steps, where k is 
# non-negative.

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    results = [None] * len(nums)
    for i, num in enumerate(nums):
      results[(i+k) % len(nums)] = num
    for i, result in enumerate(results):
      nums[i] = result
