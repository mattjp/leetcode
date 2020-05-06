# 169. Majority Element
#
# Given an array of size n, find the majority element. The majority element is 
# the element that appears more than floor(n/2) times.

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    d = {}
    for num in nums:
      if num not in d:
        d[num] = 1
      else:
        d[num] += 1
      if d[num] > (n/2):
        return num
      
# Solved again
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    from collections import Counter
    return Counter(nums).most_common()[0][0]
