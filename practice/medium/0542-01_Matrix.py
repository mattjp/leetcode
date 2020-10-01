class Solution:
  def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    """
    for each cell, BFS until you hit 0 or hit a cell that has hit 0
    """
        
    def search(matrix, lowest, i, j):
      queue = deque([(i,j,0)]) # row, col, steps
      visited = set()
      L = None
      
      while queue:
        row, col, steps = queue.popleft()
        
        for new_row, new_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
          if (
            new_row >= 0 and
            new_col >= 0 and 
            new_row < len(matrix) and 
            new_col < len(matrix[0]) and
            (new_row, new_col) not in visited
          ):            
            if lowest[new_row][new_col] == 0: # can be improved by remembering old values
              return steps + 1
            queue.append((new_row, new_col, steps + 1))
            visited.add((new_row, new_col))
            
      return -1
    
    
    lowest = [[None] * len(matrix[0]) for _ in range(len(matrix))]
    
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
          lowest[i][j] = 0
    
    for i in range(len(lowest)):
      for j in range(len(lowest[0])):
        if lowest[i][j] == None:
          lowest[i][j] = search(matrix, lowest, i, j)

    return lowest
