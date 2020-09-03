class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
      """
      Do not return anything, modify matrix in-place instead.
      """
      L = len(matrix)
      
      # transpose (row, col) -> (col, row)
      for i in range(L):
        for j in range(i,L):
          tmp = matrix[i][j]
          matrix[i][j] = matrix[j][i]
          matrix[j][i] = tmp

      # reverse
      for i in range(L):
        matrix[i].reverse()
