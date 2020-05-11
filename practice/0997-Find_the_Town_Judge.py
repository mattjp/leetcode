class Solution:
  def findJudge(self, N: int, trust: List[List[int]]) -> int:
    trusted = [0] * (N+1) # must have 1 entry that has length = trust.length
    trusts = [0] * (N+1) # must have 1 entry with same index = 0
    for t in trust:
      trusted[t[1]] += 1
      trusts[t[0]] += 1
    for i in range(1, N+1):
      if trusted[i] == N-1 and trusts[i] == 0:
        return i
    return -1
