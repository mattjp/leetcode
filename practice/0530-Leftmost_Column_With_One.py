# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
  def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

    def binaryRowSearch(row: int, min_l: int, l: int, r: int) -> int:
        m = (l + r) // 2
        x = binaryMatrix.get(row, m)
        if m == l or m == r:
          if x == 1:
            return m
          else:
            return min_l
        if x == 1:
          # min_l = m
          # go left
          return binaryRowSearch(row, m, l, m)
        if x == 0:
          # go right
          return binaryRowSearch(row, min_l, m, r)

    dims = binaryMatrix.dimensions()
    rows = dims[0]
    cols = dims[1]
    left_most = -1

    for row in range(rows):
      row_left_most = binaryRowSearch(row, -1, 0, cols)
      if left_most == -1:
        left_most = row_left_most
      else:
        left_most = min(left_most, row_left_most) if row_left_most > -1 else left_most
    return left_most
