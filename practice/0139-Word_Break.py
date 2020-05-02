# 139. Word Break
# 
# Given a non-empty string s and a dictionary wordDict containing a list of 
# non-empty words, determine if s can be segmented into a space-separated 
# sequence of one or more dictionary words.
#
# Note:
#   - The same word in the dictionary may be reused multiple times in the 
#   segmentation.
#   - You may assume the dictionary does not contain duplicate words.

class Solution:
  def wordBreakWrapper(self, s: str, wordDict: List[str], checked) -> bool:
    if s == "":
        return True
    for word in wordDict:
      if word in s and s not in checked:
        i = s.find(word)
        j = i + len(word)
        sl = s[:i]
        sr = s[j:]
        rl = self.wordBreakWrapper(sl, wordDict, checked)
        rr = self.wordBreakWrapper(sr, wordDict, checked)
        if rl and rr:
          return True
    checked.add(s)
    return False

  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    checked = set()
    return self.wordBreakWrapper(s, wordDict, checked)
