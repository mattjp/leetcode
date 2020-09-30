# this is sub-optimal
# should do DFS and save results of previous calculations in a 2D matrix
class Solution:
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    from collections import deque
    
    if not matrix:
      return 0
    
    # (i, j, steps)
    queue = deque([(i,j, 1) for j in range(len(matrix[0])) for i in range(len(matrix))])
    visited = set()
    longest = 1
    
    
    while queue:
      r, c, steps = queue.popleft()
      # print(r,c)
      
      for i,j in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        if (
          i >= 0 and
          j >= 0 and
          i < len(matrix) and
          j < len(matrix[0]) and
          (i, j, steps+1) not in visited and
          matrix[i][j] > matrix[r][c]
        ):
          queue.append((i,j,steps+1))
          visited.add((i,j,steps+1))
          longest = max(longest, steps+1)
      
      
    return longest
