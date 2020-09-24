class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    from collections import deque
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # don't include (0,0)
    start = [(0,0,1)]
    queue = deque(start) # (row, col, steps)
    seen = set(start) # (row, col)
    m, n = len(grid)-1, len(grid[0])-1
    
    # catch impossible cases before iteration
    if grid[0][0] == 1 or grid[m][n] == 1: 
      return -1
    
    while queue:
      row, col, steps = queue.popleft()
      if row == m and col == n: # catch row=0, col=0 case
        return steps
      
      for i,j in directions:
        new_row, new_col = row+i, col+j
        if (new_row == m and new_col == n):
          return steps+1
        if (
          new_row >= 0 and
          new_col >= 0 and
          new_row <= m and
          new_col <= n and
          (new_row, new_col) not in seen and
          grid[new_row][new_col] == 0
        ):
          seen.add((new_row, new_col))
          queue.append((new_row, new_col, steps+1))
          
    return -1
