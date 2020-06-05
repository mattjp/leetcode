class Solution:

  from random import choices

  def __init__(self, w: List[int]):
    self.population = range(len(w))
    self.weights = []
    total_weight = sum(w)
    for weight in w:
      self.weights.append(weight/total_weight)


  def pickIndex(self) -> int:
    return choices(self.population, self.weights)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
