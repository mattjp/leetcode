class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    from collections import Counter

    r_dict = Counter(ransomNote)
    m_dict = Counter(magazine)

    for k,v in r_dict.items():
      if k not in m_dict:
        return False
      if m_dict[k] < v:
        return False
    return True
