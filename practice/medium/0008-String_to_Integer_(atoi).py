class Solution:
  def myAtoi(self, str: str) -> int:
    """
    this problem is basically entirely edge cases
    1. strip whitespace
    2. if the first character is non-numeric, return
    3. iterate until out of numeric characters
    4. return up to the iteration point if it is within the bounds of an integer
    """
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    allowed = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+'])
    allowed_numeric = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

    s = str.strip()

    if not s or s[0] not in allowed:
      return 0

    i = 0 if s[0] != '-' and s[0] != '+' else 1
    itr = False
    while i < len(s) and s[i] in allowed_numeric:
      i += 1
      itr = True

    r = int(s[:i]) if itr else 0
    if r > INT_MAX: return INT_MAX
    elif r < INT_MIN: return INT_MIN
    else: return r
        
