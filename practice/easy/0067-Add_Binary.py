class Solution:
  def addBinary(self, a: str, b: str) -> str:
    """
    actually solving the problem
    """
    l = max(len(a), len(b))
    while len(a) < l: a = '0' + a
    while len(b) < l: b = '0' + b
    carry = 0
    output = ''
    for i in range(l-1, -1, -1):
      x = int(a[i]) if i < len(a) else 0
      y = int(b[i]) if i < len(b) else 0
      z = x + y + carry
      output = str(z % 2) + output
      carry = 1 if z > 1 else 0

    if carry:
      output = str(carry) + output

    return output


  def addBinaryShort(self, a: str, b: str) -> str:
    """
    do it the easy way
    """
    return bin(int(a,2) + int(b, 2))[2:]
