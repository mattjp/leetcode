# 268. Missing Number
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find 
# the one that is missing from the array.


class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    max_num = max(nums)
    min_num = min(nums)
    num_sum = sum(nums)
    sum_actual = sum(range(max_num+1))
    if min_num != 0:
      return 0
    if sum_actual == num_sum:
      return max_num+1
    return sum_actual - num_sum

  
# solved again
class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    expected_sum = sum(range(len(nums)+1))
    actual_sum = sum(nums)
    return expected_sum - actual_sum
  
