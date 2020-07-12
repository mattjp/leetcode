class Solution:
  def reverseBits(self, n: int) -> int:
    r = bin(n)[2:][::-1]
    while len(r) < 32: r += '0'
    return int(r, 2)
