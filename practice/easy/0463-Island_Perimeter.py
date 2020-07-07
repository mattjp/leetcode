class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
        
      def get_num_water_sides(grid: List[List[int]], i: int, j: int) -> int:
        output = 4
        if i > 0 and grid[i-1][j] == 1: output -= 1
        if i < len(grid)-1 and grid[i+1][j] == 1: output -= 1
        if j > 0 and grid[i][j-1] == 1: output -= 1
        if j < len(grid[0])-1 and grid[i][j+1] == 1: output -= 1
        return output

      output = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j] == 1:
            output += get_num_water_sides(grid, i, j)
      return output
