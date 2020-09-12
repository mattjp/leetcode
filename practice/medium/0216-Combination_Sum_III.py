class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    """
    search space is very small, so we can just DFS
    """
    self.all_combos = []
    
    def find_combos(start: int, count: int, prev: List[int]):
      if len(prev) > k or count > n:
        return
      if len(prev) == k and count == n:
        self.all_combos.append(prev.copy())
        return
      for i in range(start, 10):
        prev.append(i)
        count += i
        find_combos(i+1, count, prev)
        count -= i
        prev.pop()


    find_combos(1, 0, [])
    return self.all_combos
