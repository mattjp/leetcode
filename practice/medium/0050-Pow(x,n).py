class Solution:
  def myPow(self, x: float, n: int) -> float:
    ans = 1.0
    
    # dumb TLE conditions
    if x == ans: return x
    if x == -ans: return x if abs(n) % 2 else -x
    
    if n != 0:
      for _ in range(abs(n)):
        prev = ans
        ans *= x
        if ans == prev: break # stop cycling between -1 and 1
      if n < 0 and ans:
        ans = 1.0 / ans

    return ans
