# 20. Valid Parentheses
# 
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#   - Open brackets must be closed by the same type of brackets.
#   - Open brackets must be closed in the correct order.
#   - Note that an empty string is also considered valid.


class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    for c in s:
      if c == "(" or c == "[" or c == "{":
        stack.append(c)
      else:
        if len(stack) < 1:
          return False
        top = stack.pop()
        if c == ")" and top != "(":
          return False
        if c == "]" and top != "[":
          return False
        if c == "}" and top != "{":
          return False
    if len(stack) < 1:
      return True
    return False
