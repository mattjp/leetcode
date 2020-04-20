class Solution:

  def stringShift(self, s: str, shift: List[List[int]]) -> str:
  
    def shiftOp(s: str, direction: int, amount: int) -> str:
      amount = -amount if direction else amount
      left = s[:amount]
      right = s[amount:]
      return right + left
      
    result = s
    for sh in shift:
      result = shiftOp(result, sh[0], sh[1])
    return result
      
