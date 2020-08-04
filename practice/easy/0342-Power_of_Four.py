# dumb solution
class Solution:
  def isPowerOfFour(self, num: int) -> bool:
    if num <= 0: return False
    x = 1
    while x <= num:
      if x == num: return True
      x *= 4
    return False

# no loops
class Solution:
  def isPowerOfFour(self, num: int) -> bool:

    # 100
    # 10000
    # 1000000

    b = bin(num)[2:]

    w = num > 0
    x = b[0] == '1'
    y = len(b[1:]) % 2 == 0
    z = int(b[1:]) == 0 if b[1:] else True

    return True if w and x and y and z else False
