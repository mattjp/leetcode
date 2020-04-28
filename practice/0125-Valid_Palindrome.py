# 125. Valid Palindrome
#
# Given a string, determine if it is a palindrome, considering only alphanumeric
# characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.

class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = s.translate(str.maketrans("", "", string.punctuation))
    s = s.replace(" ", "")
    s = s.lower()
    l, r = 0, len(s)-1
    while l < r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True
