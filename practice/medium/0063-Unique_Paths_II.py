class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    """
    build from bottom right corner up
    obstacles will have zero possible paths
    """
    
    m = len(obstacleGrid)
    if not m:
      return 0
    
    n = len(obstacleGrid[0])
    if not n:
      return 1
    
    # if the target is an obstacle, quit early
    if obstacleGrid[m-1][n-1] == 1:
      return 0
    
    # initialize new 2D array of number of possible ways to reach a cell
    possible = [[None] * n for _ in range(m)]
    possible[m-1][n-1] = 1
    
    # set right column
    for i in range(m-2, -1, -1):
      if obstacleGrid[i][n-1] == 0 and possible[i+1][n-1] != 0:
        possible[i][n-1] = 1
      else:
        possible[i][n-1] = 0
      
    # set bottom row
    for j in range(n-2, -1, -1):
      if obstacleGrid[m-1][j] == 0 and possible[m-1][j+1] != 0:
        possible[m-1][j] = 1
      else:
        possible[m-1][j] = 0

    # fill in rest of grid
    for i in range(m-2, -1, -1):
      for j in range(n-2, -1, -1):
        
        if obstacleGrid[i][j] == 1:
          possible[i][j] = 0
        else:
          possible[i][j] = possible[i+1][j] + possible[i][j+1]
          
    return possible[0][0]
