class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    self.max_i = len(grid)-1
    self.max_j = len(grid[0])-1
    self.dist_to_end = {
      (self.max_i, self.max_j): grid[self.max_i][self.max_j]
    }

    def loop(grid: List[List[int]], i: int, j: int) -> int:
      if i < self.max_i:
        if (i+1,j) in self.dist_to_end:
          self.dist_to_end[(i,j)] = grid[i][j] + self.dist_to_end[(i+1,j)]
        else:
          loop(grid, i+1, j)
      if j < self.max_j:
        if (i,j+1) in self.dist_to_end:
          self.dist_to_end[(i,j)] = grid[i][j] + self.dist_to_end[(i,j+1)]
        else:
          loop(grid, i, j+1)
      if (i+1,j) in self.dist_to_end and (i,j+1) in self.dist_to_end:
        min_dist_to_end = min(self.dist_to_end[(i+1,j)], self.dist_to_end[(i,j+1)])
        self.dist_to_end[(i,j)] = grid[i][j] + min_dist_to_end
      elif (i+1,j) in self.dist_to_end:
        self.dist_to_end[(i,j)] = grid[i][j] + self.dist_to_end[(i+1,j)]
      elif (i,j+1) in self.dist_to_end:
        self.dist_to_end[(i,j)] = grid[i][j] + self.dist_to_end[(i,j+1)]
      else:
        self.dist_to_end[(i,j)] = grid[i][j]

    loop(grid, 0, 0)
    return self.dist_to_end[(0, 0)]
