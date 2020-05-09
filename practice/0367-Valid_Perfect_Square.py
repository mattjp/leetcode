class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    upper_bound = (num // 2) + 2
    for i in range(1, upper_bound):
      if i*i == num:
        return True
      if i*i > num:
        return False
    return False
