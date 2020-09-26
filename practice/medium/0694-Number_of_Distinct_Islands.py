class Solution:
  def numDistinctIslands(self, grid: List[List[int]]) -> int:    
    self.visited = set()
    self.island_shapes = set()
    self.m = len(grid)
    self.n = len(grid[0])

    def get_island_shape(grid: List[List[int]], i: int, j: int, shape: str, ch: str='S', d: int=0) -> str:
      """
      record movements and depth for each iteration
      return a string containing all movements/depths
      this string defines the shape of an island
      """
      if (
        i < 0 or
        j < 0 or
        i >= self.m or
        j >= self.n or
        (i,j) in self.visited or
        grid[i][j] == 0
      ):
        return shape
      
      shape += ch+str(d)
      self.visited.add((i,j))

      shape = get_island_shape(grid, i-1, j, shape, 'U', d+1)
      shape = get_island_shape(grid, i+1, j, shape, 'D', d+1)
      shape = get_island_shape(grid, i, j-1, shape, 'L', d+1)
      shape = get_island_shape(grid, i, j+1, shape, 'R', d+1)
      return shape

    # for each cell, check if it is the beginning of an unchecked island
    # if it is, find the shape of the island
    for i in range(self.m):
      for j in range(self.n):
        if grid[i][j] == 1 and (i,j) not in self.visited:
          island_shape = get_island_shape(grid, i, j, '')
          if island_shape not in self.island_shapes:
            self.island_shapes.add(island_shape)
            
    return len(self.island_shapes)
