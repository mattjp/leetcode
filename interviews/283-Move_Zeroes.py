# 283. Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i, zero_count = 0, 0
    while len(nums) > 0 and i < len(nums):
      if nums[i] == 0:
        nums.pop(i)
        zero_count += 1
      else:
        i += 1
    for i in range(zero_count):
      nums.append(0)
