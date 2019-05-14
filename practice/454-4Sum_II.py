# 454. 4Sum II
#
# Given four lists A, B, C, D of integer values, compute how many tuples 
# (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

class Solution:
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    AB = {}
    for a in A:
      for b in B:
        x = a + b
        if x not in AB:
          AB[x] = 1
        else:
          AB[x] += 1

    res = 0
    for c in C:
      for d in D:
        x = (c + d) * -1
        if x in AB:
          res += AB[x]
    return res
