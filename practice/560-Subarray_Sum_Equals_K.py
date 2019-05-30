# 560. Subarray Sum Equals K
#
# Given an array of integers and an integer k, you need to find the 
# total number of continuous subarrays whose sum equals to k.

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    sums = []
    cur_sum = 0
    for num in nums:
      cur_sum += num
      sums.append(cur_sum)
    res = 0
    possible = {0: 1}
    for s in sums:
      target = s - k
      if target in possible:
        res += possible[target]
      if s not in possible:
        possible[s] = 0
      possible[s] += 1
    return res
