# 242. Valid Anagram
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.

from collections import Counter
class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return Counter(s) == Counter(t)
