class Solution:
  def cutOffTree(self, forest: List[List[int]]) -> int:
    """
    0. while there are trees to cut down
    1. walk to coordinates of next tree; cut down - do BFS dummy
    2. if tree is unreachable - return
    """

    from collections import deque
    from sortedcontainers import SortedDict

    def go_to_tree(grid, i, j, tree) -> int:
      queue = deque([(i, j, 0)]) # (i, j, steps)
      visited = set()  
      while queue:
        row, col, steps = queue.popleft()
        if (row, col) == tree:
          return steps
        for r,c in [(1,0), (-1,0), (0,1), (0,-1)]:
          new_row, new_col = row+r, col+c
          if (
            new_row < len(grid) and
            new_col < len(grid[0]) and 
            new_row > -1 and 
            new_col > -1 and
            (new_row, new_col) not in visited and
            grid[new_row][new_col] != 0
          ):
            if (new_row, new_col) == tree:
              return steps+1
            visited.add((new_row, new_col))
            queue.append((new_row, new_col, steps+1))
            
      return None
    
    
    trees = SortedDict()
    
    for i in range(len(forest)):
      for j in range(len(forest[i])):
        if forest[i][j] > 1:
          trees[forest[i][j]] = (i,j)
    
    total_steps = 0
    i = j = 0
    for h,tree in trees.items():
      steps = go_to_tree(forest, i, j, tree)
      if steps == None:
        return -1
      total_steps += steps
      i,j = tree
      
    return total_steps
