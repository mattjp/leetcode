class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    """
    BFS through all oranges using double while-loop
    Update minute counter for every new BFS iteration
    """
    from collections import deque
    
    max_i = len(grid)
    max_j = len(grid[0])
    
    # get all currently rotten oranges
    rotten = deque([(i,j) for i in range(max_i) for j in range(max_j) if grid[i][j] == 2])
    
    # get all currently fresh oranges
    fresh = set([(i,j) for i in range(max_i) for j in range(max_j) if grid[i][j] == 1])
    
    mins = 0
    while rotten:

      # all new rotten oranges at the current minute
      new_rotten = deque()
      while rotten:
        # current rotten coordinates
        (i,j) = rotten.popleft()
        # check all neighbors
        if (i+1,j) in fresh:
          new_rotten.append((i+1,j))
          fresh.remove((i+1,j))
        if (i-1,j) in fresh:
          new_rotten.append((i-1,j))
          fresh.remove((i-1,j))
        if (i,j+1) in fresh:
          new_rotten.append((i,j+1))
          fresh.remove((i,j+1))
        if (i,j-1) in fresh:
          new_rotten.append((i,j-1))
          fresh.remove((i,j-1))
          
      # once all old rotten are check, update rotten to be all newly rotten oranges
      rotten = new_rotten
      
      # only update minute if any new rotten oranges were added
      mins = mins + 1 if new_rotten else mins
    
    # if there are any fresh oranges left, the problem is impossible
    return mins if len(fresh) == 0 else -1
