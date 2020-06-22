class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
    # edge cases
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return []
    
    # globals
    output = []
    matrix_size = len(matrix) * len(matrix[0])
    top    = 0
    right  = len(matrix[0])-1
    bottom = len(matrix)-1
    left   = 0
    
    # return the top row of the matrix, left-to-right
    def getTop():
      return matrix[top][left:right+1]
    
    # return the bottom row of the matrix, right-to-left
    def getBottom():
      return list(reversed(matrix[bottom][left:right+1]))
    
    # return the rightmost column of the matrix, top-to-bottom
    def getRight():
      return [m[right] for m in matrix[top:bottom+1]]
    
    # return the leftmost column of the matrix, bottom-to-top
    def getLeft():
      return [m[left] for m in matrix[bottom:top-1:-1]]
    
    # iterate until everything has been added to the output
    # add a row or column, then increment or decrement the row/column counter such that
    # values are not added more than once
    while len(output) < matrix_size:
      if top <= bottom:
        output.extend(getTop())
        top += 1
      if right >= left:
        output.extend(getRight())
        right -= 1
      if bottom >= top:
        output.extend(getBottom())
        bottom -= 1
      if left <= right:
        output.extend(getLeft())
        left += 1
      
    return output
