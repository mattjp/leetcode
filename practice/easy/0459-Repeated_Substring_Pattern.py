class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:

    for i in range(1, (len(s) // 2)+1):
      if len(s) % i == 0:
        segments = []
        length = i
        j = 0
        while j < len(s):
          start = j
          end = j+length
          segments.append(s[start:end])
          j = end
        target = segments[0]
        if all(segment == target for segment in segments):
          return True
    return False
