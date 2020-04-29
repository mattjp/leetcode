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

# Did this problem a second time
class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    # total to be returned
    res = 0
    # current sum(0, num)
    num_sum = 0
    # hash table of sum frequencies
    # 0 -> 1 exists because a distance of zero should increment res
    sums = {0: 1}
    for num in nums:
      # calculate running sum
      num_sum += num
      # calculate distance from current sum to k
      k_dist = -(k - num_sum)
      # if we have seen the distance to k required before (in sums),
      # we can add the number of times we can get the distance to k
      if k_dist in sums:
        res += sums[k_dist]
      # if we have never seen this sum before, add it
      # otherwise, increment the number of times we can get to this sum
      if num_sum not in sums:
        sums[num_sum] = 0
      sums[num_sum] += 1
    return res
