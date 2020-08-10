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
  
# solved again
class Solution:
def orangesRotting(self, grid: List[List[int]]) -> int:

    # `ripe` and `will_rot` are both mutable, therefore are passed by reference
    def rot_if_possible(i, j, ripe, will_rot):
      if (i,j) in ripe:
        ripe.remove((i,j))
        will_rot.append((i,j))


    rows = len(grid)
    cols = len(grid[0])

    rotten = [(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2]
    ripe = set([(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 1])
    will_rot = []

    time = 0
    while time == 0 or will_rot:
      will_rot = []
      while rotten:
        i,j = rotten.pop()
        rot_if_possible(i+1, j, ripe, will_rot)
        rot_if_possible(i-1, j, ripe, will_rot)
        rot_if_possible(i, j+1, ripe, will_rot)
        rot_if_possible(i, j-1, ripe, will_rot)
      rotten = will_rot
      time += 1

    # `time-1` because the `while` loop will always overshoot by one
    return time-1 if not ripe else -1
