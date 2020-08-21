class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    evens = list(filter(lambda x: x % 2 == 0, A))
    odds  = list(filter(lambda x: x % 2 == 1, A))
    evens.extend(odds)
    return evens
