class Solution:
  def climbStairs(self, n: int) -> int:
    ways = [0, 1, 2]
    if n < 3:
      return ways[n]

    for i in range(3, n+1):
      ways.append(ways[i-1] + ways[i-2])

    return ways[-1]
