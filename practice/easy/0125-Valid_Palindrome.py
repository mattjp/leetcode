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
  

# solved again
class Solution:
  def isPalindrome(self, s: str) -> bool:
    exclude = set(string.punctuation)
    exclude.add(' ')
    sp = [ch.lower() for ch in s if ch not in exclude]

    l = 0
    r = len(sp)-1
    while l < r:
      if sp[l] != sp[r]:
        return False
      l += 1
      r -= 1
    return True
