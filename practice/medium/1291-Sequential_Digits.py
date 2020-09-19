class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    from sortedcontainers import SortedSet
    self.output = SortedSet() # fancy boi
    
    def generate(cur: int, lo: int, hi: int) -> None:
      """
      generate the next sequential number by shifting all digits left by 1
      and adding 1 + least significant digit
      """
      if cur >= lo and cur <= hi and cur not in self.output:
        self.output.add(cur)
      
      if cur > hi:
        return
      
      # least-significant digit. stop if 9, since after 9, cur can't be sequential
      cur_ls = int(str(cur)[-1])
      if cur_ls == 9:
        return
      
      # shift over and recurse
      nxt = (cur * 10) + cur_ls + 1
      generate(nxt, lo, hi)
      
    
    # this is probably doing some extra work
    for i in range(10):
      generate(i, low, high)

    return list(self.output)
