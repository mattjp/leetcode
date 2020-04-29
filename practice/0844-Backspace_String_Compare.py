class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    sres = []
    tres = []
    for s in S:
      if s == '#' and len(sres) > 0:
        sres.pop()
      elif s != '#':
        sres.append(s)
    for t in T:
      if t == '#' and len(tres) > 0:
        tres.pop()
      elif t != '#':
        tres.append(t)
    return sres == tres
