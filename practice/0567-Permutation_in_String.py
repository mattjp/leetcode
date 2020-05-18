class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    # I think Counter is fast enough to let leetcode accept the dumb solution
    # Should have used a sliding window -
    # i.e. hashmap that adds/deletes a character with every increment of `i`
    from collections import Counter
    if len(s2) < len(s1):
      return False

    s1_counter = Counter(s1)
    j = len(s1)
    for i in range(len(s2)):
      tmp = s2[i:j+i]
      tmp_counter = Counter(tmp)
      if tmp_counter == s1_counter:
        return True
    return False
