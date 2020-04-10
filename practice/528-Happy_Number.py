class Solution:
    
    from collections import deque
    
    def separateN(self, n: int) -> List[int]:
      ns: int = n
      res = deque()
      while ns > 0:
        res.appendleft(ns % 10)
        ns //= 10
      return list(res)
    
    def sumSquares(self, l: List[int]) -> int:
      ls: List[int] = map(lambda x: x*x, l)
      return sum(ls)
    
    def loop(self, n: int, seen) -> bool:
      if n == 1:
        return True
      ns: List[int] = self.separateN(n)
      nsum: int = self.sumSquares(ns)
      if nsum in seen:
        return False
      seen.add(nsum)
      return self.loop(nsum, seen)
        
    
    def isHappy(self, n: int) -> bool:
      return self.loop(n, set())
