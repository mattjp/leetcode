class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    counter = collections.Counter({'0': 0, '1': 0})
    xor = bin(x ^ y)[2:] # remove '0b'
    counter.update(xor)
    return counter['1']
