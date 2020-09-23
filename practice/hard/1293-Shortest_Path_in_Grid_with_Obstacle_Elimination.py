class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    """
    DFS
    if next step is an obstacle subtract from k
    WRONG - DO IT AS BFS
    queue - [((i, j, k), s)]
    warning - this whole thing is really fuckin' ugly
    """
    from collections import deque
    
    start = ((0,0,k),0)
    queue = deque([start]) # ((i, j, k), steps)
    visited = set([start])
    m = len(grid)-1
    n = len(grid[0])-1
    
    while queue:
      loc, steps = queue.popleft()
      i,j,cur_k = loc
      if i == m and j == n:
        return steps
      
      for r,c in [(1,0), (-1,0), (0,1), (0,-1)]: # everything below this point is an absolute trainwreck
        R = i+r
        C = j+c
        if (
          R < 0 or
          C < 0 or
          R > m or
          C > n
        ):
          continue
        
        q = cur_k
        if grid[R][C] == 1:
          q -= 1
        
        if q < 0 or (R,C,q) in visited:
          continue
          
        visited.add((R,C,q))
        queue.append(((R, C, q), steps+1))
        
    return -1
