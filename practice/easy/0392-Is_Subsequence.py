class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    j = 0
    for i in t:
      if j == len(s):
        return True
      if i == s[j]:
        j += 1
    if j == len(s):
      return True 
    return False
  
# solved again
class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    i = 0
    if len(s) == 0:
      return True
    for cht in t:
      if cht == s[i]:
        i += 1
        if i == len(s):
          return True
        
    return False
