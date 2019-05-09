# 441. Arranging Coins
# 
# You have a total of n coins that you want to form in a staircase shape, where 
# every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.

class Solution:
  def arrangeCoins(self, n: int) -> int:
    i = 1
    res = 0
    while i <= n:
      res += 1
      n -= i
      i += 1
    return res
