# dumb solution
class Solution:
  def isPowerOfFour(self, num: int) -> bool:
    if num <= 0: return False
    x = 1
    while x <= num:
      if x == num: return True
      x *= 4
    return False
