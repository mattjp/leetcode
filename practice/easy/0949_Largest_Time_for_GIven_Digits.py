# should have just enumerated all permutations of indicies!
class Solution:
  def largestTimeFromDigits(self, A: List[int]) -> str:
    best = None

    for i in range(len(A)):
      for j in range(len(A)):
        index = [0, 1, 2, 3]
        if i != j:
          index.remove(i)
          index.remove(j)
          k = index.pop()
          l = index.pop()

          h = A[i]*10 + A[j]
          m1 = A[k]*10 + A[l]
          m2 = A[l]*10 + A[k]

          if h > 23:
            continue

          m = None
          if m1 < 60:
            m = m1
          if m2 < 60:
            if m == None:
              m = m2
            else:
              m = max(m, m2)

          if m != None:
            x = h*100 + m
            if best:
              best = max(best, x)
            else:
              best = x

    if best != None:
      best_str = str(best)
      while len(best_str) < 4:
        best_str = '0' + best_str
      return best_str[:2]+':'+best_str[2:]
    else:
      return ''
