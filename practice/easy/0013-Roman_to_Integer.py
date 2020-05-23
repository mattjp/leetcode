class Solution:
  def romanToInt(self, s: str) -> int:
    self.mapping = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    output = 0
    stack = list(reversed(s)) # returns reversed list of single characters
    while len(stack) > 1:
      l = stack.pop()
      r = stack.pop()
      x = self.mapping[l]
      y = self.mapping[r]
      if x < y:
        output += y - x
      else:
        output += x
        stack.append(r)

    if len(stack) == 1:
      output += self.mapping[stack.pop()]            

    return output
