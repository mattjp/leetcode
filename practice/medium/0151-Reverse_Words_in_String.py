class Solution:
  def reverseWords(self, s: str) -> str:
    t = s.strip().rstrip() # remove lead/trail whitespace 
    u = list(reversed(t.split(' '))) # split at space and reverse
    v = list(filter(lambda x: x and x != ' ' and x != '', u)) # filter out non-words
    return ' '.join(v) # return list as string
