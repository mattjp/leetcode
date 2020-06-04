class Solution:
  def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l = 0
    r = len(s)-1
    tmp = ''
    while l < r:
      tmp = s[l]
      s[l] = s[r]
      s[r] = tmp
      l += 1
      r -= 1
