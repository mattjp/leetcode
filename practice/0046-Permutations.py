# 46. Permutations
#
# Given a collection of distinct integers, return all possible permutations.

from itertools import permutations
class Solution(object):
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for permutation in permutations(nums):
      res.append(permutation)
    return res
  
# solved again without using cheating libraries
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    self.result = []

    def loop(available: List[int], current: List[int]) -> List[List[int]]:
        if len(available) == 0:
          self.result.append(current.copy()) # use shallow copy so it's not a bunch of refs
          return
        for i in range(len(available)):
          a = available.pop(i) 
          current.append(a)
          loop(available, current)
          current.pop()
          available.insert(i,a) # put `a` back where it came from (don't mess up loop)

    loop(nums, [])
    return self.result
