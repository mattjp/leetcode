class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:

    u = version1.split('.')
    v = version2.split('.')

    while len(u) < len(v): u.append('0')
    while len(v) < len(u): v.append('0')

    uint = list(map(int, u))
    vint = list(map(int, v))

    for ui,vi in zip(uint, vint):
      if ui > vi: return 1
      elif ui < vi: return -1

    return 0
  
  
# solved again
# did the exact same thing lol
class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    while len(v1) < len(v2): v1.append(0)
    while len(v1) > len(v2): v2.append(0)
    for u,v in zip(v1, v2):
      if u > v:   return 1
      elif u < v: return -1
    return 0
