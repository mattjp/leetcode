class Solution:
  def longestValidParentheses(self, s: str) -> int:
    """
    1. make stack of indicies of open parens
    2. when a close paren is encounted, create an interval using the index at the top of the stack
    3. combine all intervals (can be touching, doesn't have to be strictly overlapping)
    4. return interval with max distance
    """
    from collections import deque
    
    stack = []
    intervals = deque()
    
    for i,p in enumerate(s):
      if p == '(':
        stack.append(i)
      elif stack and p == ')':
        j = stack.pop()
        intervals.append((j,i)) # create an interval for a well-formed paren pair

    if not intervals: # catch '(' or ')' or ''
      return 0

    combined = deque([intervals.pop()])

    while intervals: # note that intervals is sorted by END index, not START index, so we work in reverse
      c = combined.popleft()
      i = intervals.pop()
      if c[0] <= i[1]+1: # intervals can be touching and still be part of the same solution e.g. ()()
        combined.appendleft((min(c[0], i[0]), max(c[1], i[1])))
      else:
        combined.extendleft([c,i])

    distances = list(map(lambda x: x[1]-x[0]+1, combined))
    return max(distances)
    
