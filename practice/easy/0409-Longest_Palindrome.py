class Solution:
  def longestPalindrome(self, s: str) -> int:
    heap = collections.Counter(s).most_common()
    evens = list(filter(lambda x: x[1] % 2 == 0, heap))
    odds = list(filter(lambda x: x[1] % 2, heap))
    has_odd = 1 if odds else 0
    return sum(map(lambda x: x[1], evens)) + sum(map(lambda x: x[1]-1, odds)) + has_odd
