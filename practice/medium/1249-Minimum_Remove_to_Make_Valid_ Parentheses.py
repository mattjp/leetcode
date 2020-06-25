class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    # always pop close before open
    # if you end with more opens then closes, pop opens (right to left)

    popen = '('
    pclose = ')'

    output = []
    stack = []

    # add `(` to stack, pop when `)` is encountered
    # add current characted to output list if it is not an unbalanced `)`
    for ch in s:
      if ch == popen:
        stack.append(ch)
      if ch == pclose:
        if stack:
          stack.pop()
        else:
          continue # unbalanced `)` - do not add
      output.append(ch)

    # iterate through output backwards, popping extra `(` from the output list
    # removing left-to-right will always result in a balanced string
    i = len(output)-1
    while stack:
      if output[i] == popen:
        stack.pop()
        del output[i]
      i -= 1

    return ''.join(output)
