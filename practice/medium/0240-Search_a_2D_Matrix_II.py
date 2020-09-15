class Solution:
  def searchMatrix(self, matrix, target):
    """
    start at upper right-hand corner
    binary search - if less then go left, if greater go down
    """
    if len(matrix) < 1:
      return False
    
    i, j = 0, len(matrix[0])-1
    while i < len(matrix) and j > -1:
      if matrix[i][j] < target:
        i += 1
      elif matrix[i][j] > target:
        j -= 1
      else:
        return True
      
    return False
