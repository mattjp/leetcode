class Solution:
  def sortedSquares(self, A: List[int]) -> List[int]:
    abs_A = list(map(lambda a: abs(a), A))
    sorted_abs_A = sorted(abs_A)
    return list(map(lambda a: a**2, sorted_abs_A))
