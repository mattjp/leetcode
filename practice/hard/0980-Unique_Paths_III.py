class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    """
    DFS
    if we have reached the end square, and every 0-square has been traversed, add to output
    if we reach end and there are 0-squares remaining, return
    O(4^(m*n)), BUT we came from 1 direction so it's ACTUALLY O(3^(m*n))
    """

    def DFS(i: int, j: int, end: tuple, unvisited: set, grid: List[List[int]]) -> None:
      """
      DFS - traverse all paths, stopping if:
        - i or j is OOB
        - (i,j) has been visited already in the current path
        - (i,j) is the endpoint (if all squares have been visited, increment output)
      """
      if (
        i < 0 or
        j < 0 or
        i >= len(grid) or
        j >= len(grid[0]) or
        (i,j) not in unvisited
      ):
        return

      unvisited.remove((i,j)) # we are now at (i,j)

      if (i,j) == end:
        if len(unvisited) == 0:
          self.output += 1
        unvisited.add((i,j)) # end is unvisited again
        return

      DFS(i+1, j, end, unvisited, grid) # up
      DFS(i, j+1, end, unvisited, grid) # right
      DFS(i-1, j, end, unvisited, grid) # down
      DFS(i, j-1, end, unvisited, grid) # left

      unvisited.add((i,j)) # (i,j) is now available to be used in a different path


    # set the start/end points and mark all squares that can be traversed
    self.output = 0
    unvisited = set()
    start = None
    end = None
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == -1:
          continue
        if grid[i][j] == 1:
          start = (i,j)
        elif grid[i][j] == 2:
          end = (i,j)
        unvisited.add((i,j))

    # run the DFS and return the output
    DFS(start[0], start[1], end, unvisited, grid)
    return self.output
