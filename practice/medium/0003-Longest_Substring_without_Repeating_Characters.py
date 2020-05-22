class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    start = end = output = 0
    current = s[start:end]

    while end < len(s):
      # if the new character being append is in the current longest string
      # remove characters from the front of the longest until everything is unique
      while s[end] in current:
        start += 1
        current = s[start:end]

      current = s[start:end+1]
      output = max(output, len(current))
      end += 1

    return output
