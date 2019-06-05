# 49. Group Anagrams
#
# Given an array of strings, group anagrams together.

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sorted_words = {}
    for word in strs:
      word_sorted = "".join(sorted(word))
      if word_sorted not in sorted_words:
        sorted_words[word_sorted] = []
      sorted_words[word_sorted].append(word)
    res = []
    for k, v in sorted_words.items():
      res.append(v)
    return res
