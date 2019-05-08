# 62. Unique Paths
#
# A robot is located at the top-left corner of a m x n grid. The robot can only 
# move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid.
#
# How many possible unique paths are there?

class Solution:
  # Solution one (brute force)
  def recursiveSolution(self, m: int, n: int) -> int:
    if m == 1 and n == 1:
      return 1
    if n == 1:
      return self.helper(m-1, n)
    if m == 1:
      return self.helper(m, n-1)
    return self.helper(m-1, n) + self.helper(m, n-1)

  # Solution two (dynamic programming)
  def helper(self, M, N, dp):
    for m in range(M-1, -1, -1):
      for n in range(N-1, -1, -1):
        if dp[n][m] is None:
          x = 0
          if m < M-1:
            x += dp[n][m+1]
          if n < N-1:
            x += dp[n+1][m]
          dp[n][m] = x
  return dp[0][0]
        
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [[None] * m for i in range(n)]
    dp[n-1][m-1] = 1
    return self.helper(m,n,dp)
