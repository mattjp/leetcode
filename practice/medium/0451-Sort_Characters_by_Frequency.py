class Solution:
  def frequencySort(self, s: str) -> str:
    from collections import Counter

    s_counter = Counter(s)
    output = ''
    for k,v in s_counter.most_common(len(s_counter)): # give counts back in order
      output += k*v
    return output
