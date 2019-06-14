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
