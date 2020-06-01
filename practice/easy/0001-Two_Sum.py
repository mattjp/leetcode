# 1. Two Sum
#
# Given an array of integers, return indices of the two numbers such 
# that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and 
# you may not use the same element twice.

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    sorted_nums = sorted(nums)
    left, right = 0, len(sorted_nums)-1
    value = sorted_nums[left] + sorted_nums[right]
    while value != target:
      if value < target:
        left += 1
      else:
        right -= 1
      value = sorted_nums[left] + sorted_nums[right]
    first = nums.index(sorted_nums[left])
    nums[first] = None
    second = nums.index(sorted_nums[right])
    return [first, second]

# solved again
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    complements = {}
    for i,num in enumerate(nums):
      complement = target - num
      if complement in complements:
        return [complements[complement], i]
      complements[num] = i
