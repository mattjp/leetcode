class Solution:
  def checkValidString(self, s: str) -> bool:
    open_p = '('
    close_p = ')'
    star = '*'
    counts = {
      open_p: 0,
      star: 0 
    }

    # forwards
    for c in s:
      if c == open_p:
        counts[c] += 1
      if c == star:
        counts[c] += 1
      if c == close_p:
        if counts[open_p] > 0:
          counts[open_p] -= 1
        elif counts[star] > 0:
          counts[star] -= 1
        else:
          return False
    if counts[star] < counts[open_p]:
      return False
      
    # backwards
    counts = {
      close_p: 0,
      star: 0 
    }
    for c in range(len(s)-1, -1, -1):
      if s[c] == close_p:
        counts[close_p] += 1
      if s[c] == star:
        counts[star] += 1
      if s[c] == open_p:
        if counts[close_p] > 0:
          counts[close_p] -= 1
        elif counts[star] > 0:
          counts[star] -= 1
        else:
          return False
    if counts[star] < counts[close_p]:
      return False
    return True
