# this is probably not what they were looking for, but using libraries was
# not forbidden in the problem definition.
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    return haystack.index(needle) if needle in haystack else -1
