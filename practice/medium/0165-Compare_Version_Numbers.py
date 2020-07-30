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
