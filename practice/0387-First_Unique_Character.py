# 387. First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and return it's 
# index. If it doesn't exist, return -1.


class Solution:
  def firstUniqChar(self, s: str) -> int:
    seen = set()
    for i, c in enumerate(s):
      if c not in seen:
        if s.count(c) == 1:
          return i
        else:
          seen.add(c)
    return -1
  
# Solved again
class Solution:
  def firstUniqChar(self, s: str) -> int:
    from collections import Counter
    chars = Counter(s)
    unique_chars = dict(filter(lambda v: v[1] == 1, chars.items()))
    for i in range(len(s)):
      if s[i] in unique_chars:
        return i
    return -1
