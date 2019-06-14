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
