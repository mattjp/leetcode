# 870. Advantage Shuffle
#
# Given two arrays A and B of equal size, the advantage of A with respect to B 
# is the number of indices i for which A[i] > B[i].
#
# Return any permutation of A that maximizes its advantage with respect to B.

class Solution:
  def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
    A_sorted = sorted(A)
    B_sorted = sorted((v, i) for i, v in enumerate(B))
    res = [None] * len(A)

    while len(A_sorted) > 0 and B_sorted[0][0] < A_sorted[-1]:
      i = 0
      while A_sorted[i] <= B_sorted[0][0]:
        i += 1
      a = A_sorted.pop(i)
      b, i_b = B_sorted.pop(0)
      res[i_b] = a

    while len(B_sorted) > 0:
      a = A_sorted.pop(0)
      b, i_b = B_sorted.pop(0)
      res[i_b] = a

    return res
