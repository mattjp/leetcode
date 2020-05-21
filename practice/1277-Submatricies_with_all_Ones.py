class Solution:
  def countSquares(self, matrix: List[List[int]]) -> int:
    max_i = len(matrix)
    max_j = len(matrix[0])
    output = 0

    # given upper-left coordinate and size, determine if square of ones
    def is_square(matrix, I, J, size) -> bool:
      if I+size < max_i \
      and J+size < max_j:
        for i in range(I, I+size+1):
          for j in range(J, J+size+1):
            if matrix[i][j] == 0:
              return False
        return True
      return False

    # check every matrix entry
    for i in range(max_i):
      for j in range(max_j):
        size = 0
        while(is_square(matrix, i, j, size)):
          output += 1
          size += 1

    return output
