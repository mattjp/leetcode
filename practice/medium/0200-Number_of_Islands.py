# 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    res = 0
    l = len(grid)
    if l == 0:
      return 0
    w = len(grid[0])
    for i in range(l):
      for j in range(w):
        if grid[i][j] == "1":
          s = [(i, j)]
          while len(s) > 0:
            x, y = s.pop()
            grid[x][y] = "0"
            if x > 0 and grid[x-1][y] == "1":
              s.append((x-1, y))
            if x < l-1 and grid[x+1][y] == "1":
              s.append((x+1, y))
            if y > 0 and grid[x][y-1] == "1":
              s.append((x, y-1))
            if y < w-1 and grid[x][y+1] == "1":
              s.append((x, y+1))
        res += 1
    return res
  
# solved again
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    max_i = len(grid)
    max_j = len(grid[0]) if max_i > 0 else 0
    output = 0
    self.visited = set()

    def count_island(grid, i, j) -> None:
      if i < 0 \
      or i >= max_i \
      or j < 0 \
      or j >= max_j \
      or (i,j) in self.visited \
      or grid[i][j] != '1':
        return
      self.visited.add((i,j))
      count_island(grid, i-1, j)
      count_island(grid, i+1, j)
      count_island(grid, i, j-1)
      count_island(grid, i, j+1)


    for i in range(max_i):
      for j in range(max_j):
        if grid[i][j] == '1' and (i,j) not in self.visited:
          output += 1
          count_island(grid, i, j)

    return output
