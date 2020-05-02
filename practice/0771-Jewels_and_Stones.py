class Solution:
  def numJewelsInStones(self, J: str, S: str) -> int:
    stones = {}
    for s in S:
      if s not in stones:
        stones[s] = 0
      stones[s] += 1
    jewels = 0
    for j in J:
      if j in stones:
        jewels += stones[j]
    return jewels
