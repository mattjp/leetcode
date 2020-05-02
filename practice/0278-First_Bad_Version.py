# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
  def binaryVersionSearch(self, l: int, r: int, earliest: int) -> int:
    m = (l + r) // 2
    is_bad = isBadVersion(m)
    if l == r:
      if is_bad:
        return m
      else:
        return earliest
    if is_bad:
      return self.binaryVersionSearch(l, m, m)
    else:
      return self.binaryVersionSearch(m+1, r, earliest)
            
    
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    return self.binaryVersionSearch(1, n, -1)
